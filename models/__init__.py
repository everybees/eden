from models.merchant import Merchant

if __name__ == '__main__':

    merchant1 = Merchant("Chukwu", "Chukwudi", "Nnamdi", "chuku2923@gmail.com", "Rule1989","chuku1989")
    merchant1.business_reg ="hhdhshdh"
    print(merchant1.business_reg)
    first_account_holder = merchant1.log_in("name", "hsdhh")
    print(first_account_holder)