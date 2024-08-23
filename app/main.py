import methods

if __name__ == "__main__":
    for g in range(1, 4):
        for c in range(1, 9):
            df = methods.addParentsGroup(g, c)
            methods.generateCSV(
                df, f"../csv/created/{g}{c}r_group_import_parents_account.csv"
            )
