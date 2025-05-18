from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import os
from PIL import Image

class Pdf():

    def __init__(self):
        self.w, self.h = A4
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "curriculo.pdf")
        self.c = canvas.Canvas(output_path, pagesize=A4)

    def titulo(self):
        self.c.setFont("Times-Roman", 20)
        self.c.drawString(45, self.h - 50, "Currículo")

    def topicos(self, nome, cargo, formacao, experiencia, skill, telefone):
        self.c.setFont("Times-Roman", 12)
        self.c.drawString(50, self.h - 80, f"- Nome: {nome}")
        self.c.drawString(50, self.h - 120, f"- Cargo desejado: {cargo}")
        self.c.drawString(50, self.h - 160, f"- Formação: {formacao}")
        self.c.drawString(50, self.h - 200, f"- Experiências: {experiencia}")
        self.c.drawString(50, self.h - 240, f"- Habilidades: {skill}")
        self.c.drawString(50, self.h - 800, f"- Telefone p/ contato: ({telefone[0:2]}) {telefone[2:7]}-{telefone[7:12]}")

    def imagem(self, path_foto):
        if path_foto and os.path.exists(path_foto):
            Image.open(path_foto)
            self.c.drawImage(path_foto, self.w - 200, self.h - 150, width=150, height=100)

    def save(self):
            self.c.save()

