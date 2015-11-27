Imports System.IO
Imports System.Text

Public Class frmMain

#Region "Program Variables"
    Const MAX_FILES As Integer = 10000

    Dim sAllFilter As String = "|All Files|*.*"
    Dim sFilter As String = "RPG Maker Encrypted Files|*.rgssad;*.rgss2a;*.rgss3a" & sAllFilter
    Dim sTitle As String = "Open RPG Maker Encrypted File"

    Dim sRoot As String = Application.StartupPath & "\"
    Dim sExtract As String = sRoot & "Extract\"

    Dim sOpenPath, sSavePath As String

    Dim numFiles As Integer
    Dim bVersion As Byte
    Dim iKey As Integer = 0
    Dim bAbort As Boolean = False

    ' File Data
    Dim FILE_Offset(MAX_FILES) As Integer
    Dim FILE_Size(MAX_FILES) As Integer
    Dim FILE_Key(MAX_FILES) As Integer
    Dim FILE_Name(MAX_FILES) As String

#End Region

#Region "Menu"

    Private Sub mnuOpen_Click(sender As System.Object, e As System.EventArgs) Handles mnuOpen.Click
        If OpenFileDlg(sFilter, sTitle, sOpenPath) Then
            bVersion = GetVersion(sOpenPath)

            Select Case bVersion
                Case 1
                    iKey = &HDEADCAFE
                    ReadRGSSADV1(sOpenPath)
                    Exit Select
                Case 3
                    ReadRGSSADV3(sOpenPath)
                    Exit Select
                Case -1
                    MsgBox("Error Reading file, no RGSSAD HEADER!")
                    Exit Select
                Case Else
                    MsgBox("Unknown Version: " & bVersion)
                    Exit Select
            End Select

        End If
    End Sub

    Private Sub mnuExit_Click(sender As System.Object, e As System.EventArgs) Handles mnuExit.Click
        Me.Close()
    End Sub

    Private Sub mnuExtractSelected_Click(sender As System.Object, e As System.EventArgs) Handles mnuExtractSelected.Click
        Dim x As Integer = lstItems.SelectedIndex

        If x > -1 Then
            Try
                ExtractFile(x)
            Catch ex As Exception
                MsgBox(ex.ToString)
                Exit Sub
            End Try
        End If
        MsgBox("Success!")
    End Sub

    Private Sub mnuExtractAllFiles_Click(sender As System.Object, e As System.EventArgs) Handles mnuExtractAllFiles.Click
        Me.Enabled = False

        pbFiles.Minimum = 0
        pbFiles.Maximum = numFiles - 1
        pbFiles.Value = 0

        Try
            For i As Integer = 0 To numFiles - 1

                ExtractFile(i)

                ' Update progress
                pbFiles.Value = i
                Application.DoEvents()

            Next i
        Catch ex As Exception
            MsgBox(ex.ToString)
            Me.Enabled = True
            Exit Sub
        End Try

        MsgBox("Success!")
        Me.Enabled = True
    End Sub

#End Region

#Region "I/O Files"

    Private Function GetVersion(ByVal sPath As String) As SByte
        Dim result As SByte = -1

        Dim br As New BinaryReader(File.OpenRead(sPath))

        If ReadCString(br, 7) = "RGSSAD" Then
            result = br.ReadSByte()
        End If

        br.Close()

        Return result
    End Function

    Private Sub ReadRGSSADV1(ByVal sPath As String)
        Dim length As Integer
        Dim br As New BinaryReader(File.OpenRead(sPath))
        lstItems.Items.Clear()
        numFiles = 0
        bAbort = False

        br.BaseStream.Seek(8, SeekOrigin.Begin)
        Do
            length = DecryptIntV1(br.ReadInt32())
            FILE_Name(numFiles) = DecryptNameV1(br.ReadBytes(length))
            FILE_Size(numFiles) = DecryptIntV1(br.ReadInt32())
            FILE_Offset(numFiles) = br.BaseStream.Position
            FILE_Key(numFiles) = iKey
            lstItems.Items.Add(FILE_Name(numFiles))

            br.BaseStream.Seek(FILE_Size(numFiles), SeekOrigin.Current)
            If br.BaseStream.Position = br.BaseStream.Length Then bAbort = True
            numFiles += 1
        Loop Until bAbort = True

        br.Close()
    End Sub

    Private Sub ReadRGSSADV3(ByVal sPath As String)
        Dim length As Integer
        Dim br As New BinaryReader(File.OpenRead(sPath))
        lstItems.Items.Clear()
        numFiles = 0
        bAbort = False

        br.BaseStream.Seek(8, SeekOrigin.Begin)

        iKey = br.ReadInt32()
        iKey *= 9
        iKey += 3

        Do
            FILE_Offset(numFiles) = DecryptIntV3(br.ReadInt32())
            FILE_Size(numFiles) = DecryptIntV3(br.ReadInt32())
            FILE_Key(numFiles) = DecryptIntV3(br.ReadInt32())
            length = DecryptIntV3(br.ReadInt32())

            If FILE_Offset(numFiles) = 0 Then
                bAbort = True
            Else
                FILE_Name(numFiles) = DecryptNameV3(br.ReadBytes(length))
                lstItems.Items.Add(FILE_Name(numFiles))

                numFiles += 1
            End If
        Loop Until bAbort = True

        br.Close()
    End Sub

#End Region

#Region "Functions"

    Private Function DecryptIntV1(ByVal value As Integer) As Integer
        Dim result As Integer = value Xor iKey

        iKey *= 7
        iKey += 3

        Return result
    End Function

    Private Function DecryptIntV3(ByVal value As Integer) As Integer
        Return value Xor iKey
    End Function

    Private Function DecryptNameV1(ByVal bNameEnc As Byte()) As String
        Dim result As String = ""
        Dim name_dec(bNameEnc.Length - 1) As Byte

        ' decrypt name
        For i As Integer = 0 To bNameEnc.Length - 1
            name_dec(i) = bNameEnc(i) Xor (iKey And &HFF)

            iKey *= 7
            iKey += 3
        Next i

        'decrypted name to string
        result = Encoding.UTF8.GetString(name_dec)

        Return result
    End Function

    Private Function DecryptNameV3(ByVal bNameEnc As Byte()) As String
        Dim result As String = ""
        Dim name_dec(bNameEnc.Length - 1) As Byte

        ' key to byte array
        Dim key As Byte() = BitConverter.GetBytes(iKey)

        ' decrypt name
        Dim j As Integer = 0
        For i As Integer = 0 To bNameEnc.Length - 1
            If j = 4 Then j = 0
            name_dec(i) = bNameEnc(i) Xor key(j)
            j += 1
        Next i

        'decrypted name to string
        result = Encoding.UTF8.GetString(name_dec)

        Return result
    End Function

    Private Function DecryptFileData(ByVal bFileData As Byte(), ByVal key As Integer) As Byte()
        Dim fDecrypt(bFileData.Length - 1) As Byte

        Dim iTempKey As Integer = key
        Dim bTempKey As Byte() = BitConverter.GetBytes(key)
        Dim j As Integer = 0

        For i As Integer = 0 To bFileData.Length - 1

            If j = 4 Then
                j = 0
                iTempKey *= 7
                iTempKey += 3
                bTempKey = BitConverter.GetBytes(iTempKey)
            End If

            fDecrypt(i) = bFileData(i) Xor bTempKey(j)

            j += 1
        Next i

        Return fDecrypt
    End Function

    Private Sub ExtractFile(ByVal fnmb As Integer)
        If sOpenPath <> "" Then
            Dim fData As Byte()
            Dim sOutFile As String = sExtract & FILE_Name(fnmb)

            Dim br As New BinaryReader(File.OpenRead(sOpenPath))
            br.BaseStream.Seek(FILE_Offset(fnmb), SeekOrigin.Begin)
            fData = br.ReadBytes(FILE_Size(fnmb))
            br.Close()

            If Directory.Exists(Path.GetDirectoryName(sOutFile)) = False Then
                Directory.CreateDirectory(Path.GetDirectoryName(sOutFile))
            End If

            DeleteFileIfExist(sOutFile)

            Dim bw As New BinaryWriter(File.OpenWrite(sOutFile))

            If bVersion = 1 Or bVersion = 3 Then
                bw.Write(DecryptFileData(fData, FILE_Key(fnmb)))
            End If

            bw.Close()

        End If
    End Sub

#End Region

#Region "Form"

    Private Sub lstItems_SelectedIndexChanged(sender As System.Object, e As System.EventArgs) Handles lstItems.SelectedIndexChanged
        Dim x As Integer = lstItems.SelectedIndex

        If x > -1 Then
            txtOffset.Text = FILE_Offset(x)
            txtSize.Text = FILE_Size(x)
            txtKey.Text = String.Format("0x{0:X8}", FILE_Key(x))
            txtName.Text = FILE_Name(x)
        End If
    End Sub

    Private Sub btnXP_Click(sender As System.Object, e As System.EventArgs) Handles btnXP.Click
        Dim sOutPath As String = sRoot & "Game.rxproj"
        DeleteFileIfExist(sOutPath)

        Dim sw As New StreamWriter(sOutPath)
        sw.Write(txtXP.Text)
        sw.Close()

    End Sub

    Private Sub btnVX_Click(sender As System.Object, e As System.EventArgs) Handles btnVX.Click
        Dim sOutPath As String = sRoot & "Game.rvproj"
        DeleteFileIfExist(sOutPath)

        Dim sw As New StreamWriter(sOutPath)
        sw.Write(txtVX.Text)
        sw.Close()

    End Sub

    Private Sub btnVXAce_Click(sender As System.Object, e As System.EventArgs) Handles btnVXAce.Click
        Dim sOutPath As String = sRoot & "Game.rvproj2"
        DeleteFileIfExist(sOutPath)

        Dim sw As New StreamWriter(sOutPath)
        sw.Write(txtVXAce.Text)
        sw.Close()

    End Sub

#End Region

End Class
