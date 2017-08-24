#coding: utf-8
from django.db import models


class projeto(models.Model):
	projeto = models.CharField(max_length=50, default="Nome do Projeto")
	nome = models.CharField(max_length=50, verbose_name='Nome')
	data = models.CharField(max_length=255, default='09 de setembro de 2017')
	linguagem = models.CharField(max_length=100, verbose_name='Linguagem')
	github = models.CharField(max_length=100, default='https://github.com/seurepositorio')
	sobre = models.TextField(max_length=255, verbose_name='Sobre')

	def _str_(self):
		return self.name
