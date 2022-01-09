# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import vonage
import requests
from LibVonage import VonageAPIs
from TestVonage.TestList import TestList
from TestVonage.TestConverse import TestConverse
from TestVonage.TestUpdate import TestUpdate

"""
def main():


    url = "https://developer.nexmo.com/jwt?application_id=ff284a6b-7942-4044-9d36-d778f0c00f91	&iat=1641620008&nbf=1641620008&exp=1644212008&jti=uq0pzJjOT3EB"

    payload = {}
    headers = {
        'alg': 'RS256',
        'typ': 'JWT',
        'Cookie': '_nexmo_developer_session=1JHj5y2LXKJfxTFqA%2Fwr6mqEvUSClVjW7AfXf7Z5yN7qJnxfo0kZYXJb4gJteVsRu1owL2rlxVWllTLKBQs3ppDkS1L0vSDAHUr7yKlsyg6aLvCyMPOYEA0ZnB0JKxQO%2BLlZQWXWYvxx7qybmct5RMrJUJ0iSqPsnYbEYqGJ9cGiGD587NuJILvdtqzQwaEB7l%2BHtx%2BHDoSAUbIbO3LAbNwldtKNJuFukycz%2BqHLiYM%3D--1aaZpliHZ7LKGGm3--5Z%2BvS%2BopvdOmSyLm3oWJVg%3D%3D'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vlist = TestList()
    vConverse = TestConverse()
    vUpdate = TestUpdate()

    ########################################################################
    ############## Test Cases #################
    ########################################################################

    #Test Case - Verifying whether the conversation exists in the list by name
    vlist.testList_names("test1")

    #Test Case - Verifying whether the conversation exists in the list by ID
    vlist.testList_ids("CON-4f48ac0b-1567-4200-af22-3034cbd56600")

    #Test Case - To verify whether a conversation is created
    vConverse.testConverse("test1011", "Product Chat112")

    vUpdate.testUpdate("updated_now", "CON-2a213e18-703e-4bf9-bdb8-f795b1dd986a", "CHAT 11")
    vlist.testList_names("updated_now")
    #test_update()

    #main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
