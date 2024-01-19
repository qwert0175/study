import pprint
import requests

def get_deposit_products():
    api_key = '1223d0a818dda43a871a5196baae546a'

    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    # 응답을 json 형태로 변환
    response = requests.get(url,params=params).json()
    return response

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # pprint.pprint(): json을 보기 좋은 형식으로 출력
    # pprint.pprint(result)



### 요구사항

# A. 데이터 추출 - Key값 출력하기
# print(result['result'].keys())

# B. 데이터 추출 - 전체 정기예금 상품 리스트
# pprint.pprint(result['result']['baseList'])

# C 데이터 가공 - 전체 정기예금 옵션 리스트
optionList = result['result']['optionList']

new_optionList = []

def make_opt_dict(data):
    opt_dic = {
        '금융상품코드': data['fin_prdt_cd'],
        '저축 금리': data['intr_rate'],
        '저축 기간': data['save_trm'],
        '저축금리유형': data['intr_rate_type'],
        '저축금리유형명': data['intr_rate_type_nm'],
        '최고 우대금리': data['intr_rate2']
    }

    return opt_dic

for opt in optionList :
    new_optionList.append(make_opt_dict(opt))

# pprint.pprint(new_optionList)


# D 데이터 가공 - 새로운 값을 만들어 반환하기

new_fin_list = []

for i in range(len(result['result']['baseList'])):
    pprint.pprint(new_optionList[i])
    # pprint.pprint(new_optionList[i]['금융상품코드'])

#     dic = {
#         '금리정보': new_optionList[i],
#         '금융상품명': result['result']['baseList'][i]['fin_prdt_nm'],
#         '금융회사명': result['result']['baseList'][i]['kor_co_nm']
#     }

    

#     new_fin_list.append(dic)

# pprint.pprint(new_fin_list)

# for opt in new_optionList:


