Imports System.IO
Imports System.Text

Module modFunctions

    Public Function OpenFileDlg(ByVal sFilter As String, ByVal sTitle As String, ByRef sPath As String) As Boolean
        Dim fOpenDlg As New OpenFileDialog

        With fOpenDlg
            .Filter = sFilter
            .FilterIndex = 1
            .InitialDirectory = Application.StartupPath
            .Title = sTitle

            Dim UserClickedOK As Boolean = .ShowDialog

            If (UserClickedOK = False) Then
                Return False
            End If

            sPath = .FileName

            If sPath = "" Then
                Return False
            End If

        End With

        Return True
    End Function

    Public Function SaveFileDlg(ByVal sFilter As String, ByVal sTitle As String, ByVal sFileName As String, ByRef sPath As String) As Boolean
        Dim fSaveDlg As New SaveFileDialog

        With fSaveDlg
            .Filter = sFilter
            .FilterIndex = 1
            .InitialDirectory = Application.StartupPath
            .Title = sTitle
            .FileName = sFileName

            Dim UserClickedOK As Boolean = .ShowDialog

            If (UserClickedOK = False) Then
                Return False
            End If

            sPath = .FileName

            If sPath = "" Then
                Return False
            End If

        End With
        Return True
    End Function

    Public Function DeleteFileIfExist(ByVal sPath As String) As Integer
        Try
            If File.Exists(sPath) Then
                File.Delete(sPath)
            End If
            Return 0
        Catch ex As Exception
            MsgBox(ex.ToString)
        End Try
        Return -1
    End Function

    Public Function ReadCString(ByVal br As BinaryReader,
                                ByVal MaxLength As Integer,
                                Optional ByVal lOffset As Long = -1,
                                Optional ByVal enc As Encoding = Nothing) As String

        Dim fTemp As Long = br.BaseStream.Position
        Dim bTemp As Byte = 0, i As Integer = 0, result As String = ""

        If lOffset > -1 Then
            br.BaseStream.Seek(lOffset, SeekOrigin.Begin)
        End If

        Do
            bTemp = br.ReadByte()
            If bTemp = 0 Then Exit Do

            i += 1
        Loop While i < MaxLength

        If lOffset > -1 Then
            br.BaseStream.Seek(lOffset, SeekOrigin.Begin)
            If enc Is Nothing Then
                result = Encoding.ASCII.GetString(br.ReadBytes(i))
            Else
                result = enc.GetString(br.ReadBytes(i))
            End If
            br.BaseStream.Seek(fTemp, SeekOrigin.Begin)
        Else
            br.BaseStream.Seek(fTemp, SeekOrigin.Begin)
            If enc Is Nothing Then
                result = Encoding.ASCII.GetString(br.ReadBytes(i))
            Else
                result = enc.GetString(br.ReadBytes(i))
            End If
            br.BaseStream.Seek(fTemp + MaxLength, SeekOrigin.Begin)
        End If

        Return result
    End Function

End Module
