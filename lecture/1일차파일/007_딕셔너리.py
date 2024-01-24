#딕셔너리 - 키값(key)과 값(value)을 쌍으로 가짐
#           키(key)값은 변하지 않는 값으로 설정이 가능
a_dict = {"a":"apple", "b":"반하나", 1:"하나", "둘":2, (1,2,3):"일,이,삼"}
print(a_dict["a"]) #a_dict[키값]
print(a_dict["b"])
print(a_dict[1])
print(a_dict[(1,2,3)])

print(a_dict.keys())
print(a_dict.values())

a_list_dict = list(a_dict.keys())
print(a_list_dict)

a_dict.clear() #딕셔너리 초기화
print(a_dict)