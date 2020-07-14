import json
import requests


def get_data(url):
    r = requests.get(url)
    company_dic = r.json()
    company_list = []
    for i in range(len(company_dic['records'])):
        company_list.append(company_dic['records'][i])
    return company_list


def get_companies():
    urls = ['https://api.data.gov.in/resource/794c42c2-8120-4fdc-8773-ec366dd0ac5a?api-key=579b464db66ec23bdd0000016e2fa803b03e4052554b7cc3237311b2&format=json&offset=0&limit=100',
            'https://api.data.gov.in/resource/c37f465a-03f1-4a38-8cf6-78375b0f9d61?api-key=579b464db66ec23bdd0000016e2fa803b03e4052554b7cc3237311b2&format=json&offset=0&limit=100',
            'https://api.data.gov.in/resource/98c6113a-cf4f-45cc-a245-5084d1b0bd59?api-key=579b464db66ec23bdd0000016e2fa803b03e4052554b7cc3237311b2&format=json&offset=0&limit=100',
            'https://api.data.gov.in/resource/11d4b398-3f85-4e5e-813c-fe105a17c02c?api-key=579b464db66ec23bdd0000016e2fa803b03e4052554b7cc3237311b2&format=json&offset=0&limit=100',
            'https://api.data.gov.in/resource/595039cd-edcd-47af-b4e4-d37a9d15b36b?api-key=579b464db66ec23bdd0000016e2fa803b03e4052554b7cc3237311b2&format=json&offset=0&limit=10',
            '']
    companies = []
    for url in urls:
        companies += get_data(url)
    return companies