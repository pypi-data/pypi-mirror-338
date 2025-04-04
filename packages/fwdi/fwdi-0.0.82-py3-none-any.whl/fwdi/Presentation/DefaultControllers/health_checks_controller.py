#        _       __        __    __________    _____     __   __     __
#   	/ \	    |  |	  |__|  |__________|  |  _  \   |__|  \ \   / /
#      / _ \	|  |	   __       |  |      | |_)  |   __    \ \_/ /   Alitrix - Modern NLP
#     / /_\ \	|  |	  |  |      |  |      |  _  /   |  |    } _ {    Languages: Python, C#
#    / _____ \	|  |____  |  |      |  |      | | \ \   |  |   / / \ \   http://github.com/Alitrix
#   /_/     \_\	|_______| |__|	    |__|      |_|  \_\  |__|  /_/   \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Alitrix Authors <http://github.com/Alitrix>
from datetime import datetime
from fastapi import Response

from ...Application.Abstractions.meta_service import MetaServiceFWDI

class HealthChecksController(metaclass=MetaServiceFWDI):
    def __init__(self):
        super().__init__()
        self.type_page = "application/xml"
        self.default_page = """default page"""
    def index(self, message:str)->Response:
        HealthChecksController.__log__(f"{__name__}:{message}")
        page = f"pong\n{datetime.now()}"
        return Response(content=page, media_type=self.type_page) # HTMLResponse(content=demo, status_code=200)