#********Nested Dictionary********
course={
    'class8':{"mode":"online", "duration":"6 month","fee":"3500"},
    'class9':{"mode":"both","duration":"8 month","fee":"4000"},
    'class10':{"mode":"online","duration":"1 year","fee":"5000"}
}
print(course["class9"])
print(course["class10"])
print(course["class10"]["fee"])#class 10th fee
print(course["class9"]["duration"])#class 9th course duration