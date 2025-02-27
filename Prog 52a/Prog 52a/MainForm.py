﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(119, 70)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(113, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Length:"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(119, 93)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(113, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Width:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Location = System.Drawing.Point(119, 172)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(376, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Area:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Location = System.Drawing.Point(119, 195)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(376, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Perimeter:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(163, 67)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(163, 90)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(50, 274)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(276, 274)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(516, 274)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self.ClientSize = System.Drawing.Size(715, 325)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog 52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		"""Notes:
		Data Types:
			-int (Integer): Whole Number
			-float (Float-point Number): Number w/ decimal
			-str (String): Text)
			
		Operators: + - * / % **(pow) //(floor divide)
		
		"""
		length = int(self._textBox1.Text)
		width = int(self._textBox2.Text)
		area = length * width
		perim = 2 * length + 2 * width
		self._label3.Text = "Area:" + str(area)
		self._label4.Text = "Perimeter:" + str(perim)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = "Area: "
		self._label4.Text = "Perimeter: "

	def Button3Click(self, sender, e):
		Application.Exit()