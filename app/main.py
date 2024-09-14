import methods

if __name__ == "__main__":
    """
    df = methods.createParentsAccount()
    methods.generateCSV(df, "../csv/created/parents_account.csv")
    """

    """
    for g in range(1, 4):
        for c in range(1, 9):
            df = methods.addParentsGroup(g, c)
            methods.generateCSV(
                df, f"../csv/created/{g}{c}r_group_import_parents_account.csv"
            )
    """

    df = methods.createGuestAccount(3000, 6001)
    methods.generateCSV(df, "../csv/created/guest_account_1.csv")
