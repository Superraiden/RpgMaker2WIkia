<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmMain
    Inherits System.Windows.Forms.Form

    'Das Formular überschreibt den Löschvorgang, um die Komponentenliste zu bereinigen.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Wird vom Windows Form-Designer benötigt.
    Private components As System.ComponentModel.IContainer

    'Hinweis: Die folgende Prozedur ist für den Windows Form-Designer erforderlich.
    'Das Bearbeiten ist mit dem Windows Form-Designer möglich.  
    'Das Bearbeiten mit dem Code-Editor ist nicht möglich.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(frmMain))
        Me.MenuStrip1 = New System.Windows.Forms.MenuStrip()
        Me.mnuFile = New System.Windows.Forms.ToolStripMenuItem()
        Me.mnuOpen = New System.Windows.Forms.ToolStripMenuItem()
        Me.ToolStripSeparator1 = New System.Windows.Forms.ToolStripSeparator()
        Me.mnuExit = New System.Windows.Forms.ToolStripMenuItem()
        Me.mnuTools = New System.Windows.Forms.ToolStripMenuItem()
        Me.mnuExtractSelected = New System.Windows.Forms.ToolStripMenuItem()
        Me.mnuExtractAllFiles = New System.Windows.Forms.ToolStripMenuItem()
        Me.StatusStrip1 = New System.Windows.Forms.StatusStrip()
        Me.pbFiles = New System.Windows.Forms.ToolStripProgressBar()
        Me.lblState = New System.Windows.Forms.ToolStripStatusLabel()
        Me.lstItems = New System.Windows.Forms.ListBox()
        Me.GroupBox2 = New System.Windows.Forms.GroupBox()
        Me.txtVXAce = New System.Windows.Forms.TextBox()
        Me.txtVX = New System.Windows.Forms.TextBox()
        Me.txtXP = New System.Windows.Forms.TextBox()
        Me.btnVXAce = New System.Windows.Forms.Button()
        Me.btnVX = New System.Windows.Forms.Button()
        Me.btnXP = New System.Windows.Forms.Button()
        Me.txtName = New System.Windows.Forms.TextBox()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.txtKey = New System.Windows.Forms.TextBox()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.txtSize = New System.Windows.Forms.TextBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.txtOffset = New System.Windows.Forms.TextBox()
        Me.MenuStrip1.SuspendLayout()
        Me.StatusStrip1.SuspendLayout()
        Me.GroupBox2.SuspendLayout()
        Me.SuspendLayout()
        '
        'MenuStrip1
        '
        Me.MenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.mnuFile, Me.mnuTools})
        Me.MenuStrip1.Location = New System.Drawing.Point(0, 0)
        Me.MenuStrip1.Name = "MenuStrip1"
        Me.MenuStrip1.Size = New System.Drawing.Size(438, 24)
        Me.MenuStrip1.TabIndex = 2
        Me.MenuStrip1.Text = "MenuStrip1"
        '
        'mnuFile
        '
        Me.mnuFile.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.mnuOpen, Me.ToolStripSeparator1, Me.mnuExit})
        Me.mnuFile.Name = "mnuFile"
        Me.mnuFile.Size = New System.Drawing.Size(37, 20)
        Me.mnuFile.Text = "&File"
        '
        'mnuOpen
        '
        Me.mnuOpen.Name = "mnuOpen"
        Me.mnuOpen.Size = New System.Drawing.Size(124, 22)
        Me.mnuOpen.Text = "&Open File"
        '
        'ToolStripSeparator1
        '
        Me.ToolStripSeparator1.Name = "ToolStripSeparator1"
        Me.ToolStripSeparator1.Size = New System.Drawing.Size(121, 6)
        '
        'mnuExit
        '
        Me.mnuExit.Name = "mnuExit"
        Me.mnuExit.Size = New System.Drawing.Size(124, 22)
        Me.mnuExit.Text = "&Exit"
        '
        'mnuTools
        '
        Me.mnuTools.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.mnuExtractSelected, Me.mnuExtractAllFiles})
        Me.mnuTools.Name = "mnuTools"
        Me.mnuTools.Size = New System.Drawing.Size(48, 20)
        Me.mnuTools.Text = "&Tools"
        '
        'mnuExtractSelected
        '
        Me.mnuExtractSelected.Name = "mnuExtractSelected"
        Me.mnuExtractSelected.Size = New System.Drawing.Size(156, 22)
        Me.mnuExtractSelected.Text = "&Extract Selected"
        '
        'mnuExtractAllFiles
        '
        Me.mnuExtractAllFiles.Name = "mnuExtractAllFiles"
        Me.mnuExtractAllFiles.Size = New System.Drawing.Size(156, 22)
        Me.mnuExtractAllFiles.Text = "&Extract All Files"
        '
        'StatusStrip1
        '
        Me.StatusStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.pbFiles, Me.lblState})
        Me.StatusStrip1.Location = New System.Drawing.Point(0, 291)
        Me.StatusStrip1.Name = "StatusStrip1"
        Me.StatusStrip1.Size = New System.Drawing.Size(438, 22)
        Me.StatusStrip1.TabIndex = 3
        Me.StatusStrip1.Text = "StatusStrip1"
        '
        'pbFiles
        '
        Me.pbFiles.Name = "pbFiles"
        Me.pbFiles.Size = New System.Drawing.Size(212, 16)
        '
        'lblState
        '
        Me.lblState.Name = "lblState"
        Me.lblState.Size = New System.Drawing.Size(39, 17)
        Me.lblState.Text = "Ready"
        '
        'lstItems
        '
        Me.lstItems.Dock = System.Windows.Forms.DockStyle.Left
        Me.lstItems.FormattingEnabled = True
        Me.lstItems.Location = New System.Drawing.Point(0, 24)
        Me.lstItems.Name = "lstItems"
        Me.lstItems.Size = New System.Drawing.Size(216, 267)
        Me.lstItems.TabIndex = 4
        '
        'GroupBox2
        '
        Me.GroupBox2.Controls.Add(Me.txtVXAce)
        Me.GroupBox2.Controls.Add(Me.txtVX)
        Me.GroupBox2.Controls.Add(Me.txtXP)
        Me.GroupBox2.Controls.Add(Me.btnVXAce)
        Me.GroupBox2.Controls.Add(Me.btnVX)
        Me.GroupBox2.Controls.Add(Me.btnXP)
        Me.GroupBox2.Controls.Add(Me.txtName)
        Me.GroupBox2.Controls.Add(Me.Label5)
        Me.GroupBox2.Controls.Add(Me.Label4)
        Me.GroupBox2.Controls.Add(Me.txtKey)
        Me.GroupBox2.Controls.Add(Me.Label3)
        Me.GroupBox2.Controls.Add(Me.txtSize)
        Me.GroupBox2.Controls.Add(Me.Label1)
        Me.GroupBox2.Controls.Add(Me.txtOffset)
        Me.GroupBox2.Dock = System.Windows.Forms.DockStyle.Right
        Me.GroupBox2.Location = New System.Drawing.Point(216, 24)
        Me.GroupBox2.Name = "GroupBox2"
        Me.GroupBox2.Size = New System.Drawing.Size(222, 267)
        Me.GroupBox2.TabIndex = 5
        Me.GroupBox2.TabStop = False
        Me.GroupBox2.Text = "File Info"
        '
        'txtVXAce
        '
        Me.txtVXAce.Font = New System.Drawing.Font("Microsoft Sans Serif", 6.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.txtVXAce.Location = New System.Drawing.Point(128, 200)
        Me.txtVXAce.Name = "txtVXAce"
        Me.txtVXAce.Size = New System.Drawing.Size(80, 18)
        Me.txtVXAce.TabIndex = 17
        Me.txtVXAce.Text = "RPGVXAce 1.00"
        '
        'txtVX
        '
        Me.txtVX.Font = New System.Drawing.Font("Microsoft Sans Serif", 6.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.txtVX.Location = New System.Drawing.Point(128, 176)
        Me.txtVX.Name = "txtVX"
        Me.txtVX.Size = New System.Drawing.Size(80, 18)
        Me.txtVX.TabIndex = 16
        Me.txtVX.Text = "RPGVX 1.02"
        '
        'txtXP
        '
        Me.txtXP.Font = New System.Drawing.Font("Microsoft Sans Serif", 6.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.txtXP.Location = New System.Drawing.Point(128, 152)
        Me.txtXP.Name = "txtXP"
        Me.txtXP.Size = New System.Drawing.Size(80, 18)
        Me.txtXP.TabIndex = 15
        Me.txtXP.Text = "RPGXP 1.02"
        '
        'btnVXAce
        '
        Me.btnVXAce.Font = New System.Drawing.Font("Microsoft Sans Serif", 6.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.btnVXAce.Location = New System.Drawing.Point(8, 200)
        Me.btnVXAce.Name = "btnVXAce"
        Me.btnVXAce.Size = New System.Drawing.Size(112, 23)
        Me.btnVXAce.TabIndex = 14
        Me.btnVXAce.Text = "Generate Game.rvproj2"
        Me.btnVXAce.UseVisualStyleBackColor = True
        '
        'btnVX
        '
        Me.btnVX.Font = New System.Drawing.Font("Microsoft Sans Serif", 6.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.btnVX.Location = New System.Drawing.Point(8, 176)
        Me.btnVX.Name = "btnVX"
        Me.btnVX.Size = New System.Drawing.Size(112, 23)
        Me.btnVX.TabIndex = 13
        Me.btnVX.Text = "Generate Game.rvproj"
        Me.btnVX.UseVisualStyleBackColor = True
        '
        'btnXP
        '
        Me.btnXP.Font = New System.Drawing.Font("Microsoft Sans Serif", 6.75!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.btnXP.Location = New System.Drawing.Point(8, 152)
        Me.btnXP.Name = "btnXP"
        Me.btnXP.Size = New System.Drawing.Size(112, 23)
        Me.btnXP.TabIndex = 12
        Me.btnXP.Text = "Generate Game.rxproj"
        Me.btnXP.UseVisualStyleBackColor = True
        '
        'txtName
        '
        Me.txtName.Location = New System.Drawing.Point(8, 40)
        Me.txtName.Name = "txtName"
        Me.txtName.Size = New System.Drawing.Size(200, 20)
        Me.txtName.TabIndex = 7
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Location = New System.Drawing.Point(8, 112)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(95, 13)
        Me.Label5.TabIndex = 5
        Me.Label5.Text = "Decrypt Base Key:"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(8, 88)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(30, 13)
        Me.Label4.TabIndex = 4
        Me.Label4.Text = "Size:"
        '
        'txtKey
        '
        Me.txtKey.Location = New System.Drawing.Point(128, 112)
        Me.txtKey.Name = "txtKey"
        Me.txtKey.Size = New System.Drawing.Size(80, 20)
        Me.txtKey.TabIndex = 11
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(8, 64)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(38, 13)
        Me.Label3.TabIndex = 3
        Me.Label3.Text = "Offset:"
        '
        'txtSize
        '
        Me.txtSize.Location = New System.Drawing.Point(128, 88)
        Me.txtSize.Name = "txtSize"
        Me.txtSize.Size = New System.Drawing.Size(80, 20)
        Me.txtSize.TabIndex = 10
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(8, 24)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(38, 13)
        Me.Label1.TabIndex = 1
        Me.Label1.Text = "Name:"
        '
        'txtOffset
        '
        Me.txtOffset.Location = New System.Drawing.Point(128, 64)
        Me.txtOffset.Name = "txtOffset"
        Me.txtOffset.Size = New System.Drawing.Size(80, 20)
        Me.txtOffset.TabIndex = 9
        '
        'frmMain
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(438, 313)
        Me.Controls.Add(Me.GroupBox2)
        Me.Controls.Add(Me.lstItems)
        Me.Controls.Add(Me.StatusStrip1)
        Me.Controls.Add(Me.MenuStrip1)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.Name = "frmMain"
        Me.Text = "RPG Maker XP / VX / VX Ace Decrypter by Falo"
        Me.MenuStrip1.ResumeLayout(False)
        Me.MenuStrip1.PerformLayout()
        Me.StatusStrip1.ResumeLayout(False)
        Me.StatusStrip1.PerformLayout()
        Me.GroupBox2.ResumeLayout(False)
        Me.GroupBox2.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents MenuStrip1 As System.Windows.Forms.MenuStrip
    Friend WithEvents mnuFile As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents mnuOpen As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents ToolStripSeparator1 As System.Windows.Forms.ToolStripSeparator
    Friend WithEvents mnuExit As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents mnuTools As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents StatusStrip1 As System.Windows.Forms.StatusStrip
    Friend WithEvents lblState As System.Windows.Forms.ToolStripStatusLabel
    Friend WithEvents pbFiles As System.Windows.Forms.ToolStripProgressBar
    Friend WithEvents lstItems As System.Windows.Forms.ListBox
    Friend WithEvents GroupBox2 As System.Windows.Forms.GroupBox
    Friend WithEvents txtName As System.Windows.Forms.TextBox
    Friend WithEvents Label5 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents txtKey As System.Windows.Forms.TextBox
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents txtSize As System.Windows.Forms.TextBox
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents txtOffset As System.Windows.Forms.TextBox
    Friend WithEvents txtVXAce As System.Windows.Forms.TextBox
    Friend WithEvents txtVX As System.Windows.Forms.TextBox
    Friend WithEvents txtXP As System.Windows.Forms.TextBox
    Friend WithEvents btnVXAce As System.Windows.Forms.Button
    Friend WithEvents btnVX As System.Windows.Forms.Button
    Friend WithEvents btnXP As System.Windows.Forms.Button
    Friend WithEvents mnuExtractSelected As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents mnuExtractAllFiles As System.Windows.Forms.ToolStripMenuItem

End Class
