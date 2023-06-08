# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:22:08 2023

@author: lydie
"""

from tkinter import *
from MySQL import MySQL
from CredentialsCtxRessources.LoginCtx import LoginCtx
from Player import Player

credentials_ctx = LoginCtx()
credentials_ctx.generate()

if credentials_ctx.get_connected() == False:
    raise RuntimeError("Impossible de se connecter")

user = Player(credentials_ctx.get_connected()[0], credentials_ctx.get_connected()[1])
