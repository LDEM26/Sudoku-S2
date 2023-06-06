# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:22:08 2023

@author: lydie
"""

from CredentialsCtxRessources.CredentialsCtx import *
from Player import *

cred = CredentialsCtx()
cred.generate()

if cred.get_connected() == False:
    raise RuntimeError("Impossible de se connecter")

user = Player(cred.get_connected()[0], cred.get_connected()[1])