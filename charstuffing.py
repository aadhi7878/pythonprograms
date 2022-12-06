inputs=input("enter the message")
sdel='DELSTX'
edel='DELETX'
inputs=inputs.upper()
inputs=inputs.replace('DEL','DELDEL')
inputs=sdel+inputs+edel
print(inputs)
decode=inputs.removeprefix('DELSTX')
decode=decode.removesuffix('DELETX')
decode=decode.replace('DELDEL','DEL')
print(decode)


