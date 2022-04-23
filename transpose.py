import pandas as pd

def main():
	pd.read_csv('cr2_prDaily_2020_ghcn.txt', header=None).T.to_csv('cr2_prDaily_2020_ghcn_T.txt', header=False, index=False)

if __name__ == "__main__":
    main()