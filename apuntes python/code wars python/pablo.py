
nm1 = str(input("deme su nombre"))
nm2 = str(input("confirme su nombre"))

nm1l = (len(nm1)-1)
nm2l = (len(nm2)-1)

if nm1[1] == nm2[1]:
    print("coincidencia")
elif nm1[nm1l] == nm2[nm2l]:
    print("coincidencia")
else:
    print("no hay coincidencia")