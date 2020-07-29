import os


def get_file_list(dir_name):  # get_file_list : 매개변수로 입력받은 파일이름을 가져오는 함수
    return os.listdir(dir_name)


get_file_list("news_data")


def get_contents(file_list):
    y_class = []
    X_text = []
    class_dict = {
        # 0 : 야구 / 1 : 축구
        1: "0", 2: "0", 3: "0", 4: "0", 5: "1", 6: "1", 7: "1", 8: "1"
    }
    for file_name in file_list:
        try:
            f = open(file_name, "r", encoding="cp949")  # cp949 : windows파일
            category = int(file_name.split(os.sep)[1].split("_")[0])
            # os.sep : os에 따른 경로를 나눌 때 /, \인지 구분해준다
            # (os.sep)[1] : 파일명(1_Dae-Ho...)
            y_class.append(class_dict[category])
            # class_dict[category] : 1~4까지는 "0"으로 설정해두었기 때문에 야구로 분류, 5~8은 축구로 분류
            X_text.append(f.read())
            # X_text : 파일의 텍스트를 읽어와서 대입
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text, y_class


def get_cleaned_text(word):
    import re
    text = re.sub('\W+', '', word.lower())  # 의미없는 문장보호 등은 제거하기
    return word


def get_corpus_dict(text):
    text = [sentence.split() for sentence in text]
    cleaned_words = [get_cleaned_text(word) for words in text for word in words]
    # for words in text:
    # for word in text: 와 동일

    from collections import OrderedDict  # OrderedDict : 값을 집어 넣은 순서대로 사용하고 싶을 때 사용
    corpus_dict = OrderedDict()
    for i, v in enumerate(set(cleaned_words)):
        corpus_dict[v] = i  # 단어들이 키값
    return corpus_dict


def get_count_vector(text, corpus):
    text = [sentence.split() for sentence in text]
    word_number_list = [[corpus[get_cleaned_text(word)] for word in words] for words in text]
    # word_number_list : 각 문서들마다 몇번째 인덱스 단어로 이루어져 있는지 나타냄 (단어->숫자)
    X_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))]
    # X_vector : 0 으로 초기화된 벡터 생성

    for i, text in enumerate(word_number_list):
        for word_number in text:
            X_vector[i][word_number] += 1 # 단어가 사용되었으면 1씩 증가시켜 몇번 사용되었는지 표시
    return X_vector


import math


def get_cosine_similarity(v1, v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i];
        y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y
    return sumxy / math.sqrt(sumxx * sumyy)


# 각 문서들이 얼마나 비슷한지 나타내는 함수
def get_similarity_score(X_vector, source): # source : 찾고자 하는 문서
    source_vector = X_vector[source]
    similarity_list = []
    for target_vector in X_vector:
        similarity_list.append(
            get_cosine_similarity(source_vector, target_vector))
    return similarity_list


# 키값으로 정렬을 하기 위한 함수
# 가장 유사한 것들을 나타내줌
def get_top_n_similarity_news(similarity_score, n):
    import operator
    x = {i: v for i, v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))

    return list(reversed(sorted_x))[1:n + 1]


def get_accuracy(similarity_list, y_class, source_news):
    source_class = y_class[source_news]

    return sum([source_class == y_class[i[0]] for i in similarity_list]) / len(similarity_list)


if __name__ == "__main__":  # 파이썬의 메인함수 선언, 시작을 의미
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    # 파일의 경로를 합쳐주기 위해 join
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
    X_text, y_class = get_contents(file_list)
    # corpus : text안에 있는 단어들의 인덱스 값
    corpus = get_corpus_dict(X_text)
    print("Number of words : {0}".format(len(corpus)))

    X_vector = get_count_vector(X_text, corpus)
    source_number = 10

    result = []

    for i in range(80):
        source_number = i

        similarity_score = get_similarity_score(X_vector, source_number)
        similarity_news = get_top_n_similarity_news(similarity_score, 10)
        accuracy_score = get_accuracy(similarity_news, y_class, source_number)
        result.append(accuracy_score)
    print(sum(result) / 80)
