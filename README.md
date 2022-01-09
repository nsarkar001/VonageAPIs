# VonageAPIs
This is a test framework for testing Coversations APIs.


main - Entry point for test case execution

Libraries - LibVonage
    VonageAPIs.py - It consists of get,post,put requests for conversation APIs

Test Methods - TestVonage
    TestList.py - This consists of implementation of test methods for list conversation APIs
        Test Methods -
            testList(self, expectedCount) - Test case to verify the conversation count
            testList_names(self, conv_name) - Test case to verify whether the conversation name exists in the list
            testList_ids(self, conv_ids) - Test case to verify whether the conversation ids exists in the list
    TestCoverse.py - This consists of implementation of test methods for create conversation API
        Test Methods -
            testConverse(self, name, display_name) - Test case to verify whether a conversation is created successfully
    TestUpdate.py - This consists of implementation of test methods for updating a conversation based on conversation id
        Test Methods -
            testUpdate(self, update_name, conv_id, update_display_name) - Test case to verify whether a conversation is created successfully

Logs - LogVonage
    TestList.log
    TestConverse.log





