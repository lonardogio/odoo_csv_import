import pandas as pd

if __name__ == '__main__':
    print("Excel Union by field")
    elenco_prodotti_id_df = pd.read_excel(r'source/elenco_prodotti_id.xlsx')
    listino_generali_df = pd.read_excel(r'source/inner_join_listino_generali_df.xls')
    listino_unisalute_df = pd.read_excel(r'source/inner_join_listino_unisalute_df.xls')

    print("Original headers")
    print("anagrafica_prestazioni_df: " + elenco_prodotti_id_df.columns.values)
    print("listino_generali_df: " + listino_generali_df.columns.values)
    print("listino_unisalute_df: " + listino_unisalute_df.columns.values)

    # change header
    # product_template_ilaria_df.columns = ['prezzo_ssn', 'listino_privato', 'name', 'codice_regionale_numerico',
    #                                    'e_una_prestazione_convenzionata', 'erogabile', 'unita_organizzativa']
    # product_template_odoo_df.columns = ['id_esterno', 'nome', 'unita_organizzativa_nome', 'unita_organizzativa_codice_interno',
    #                                    'codice_numerico_regionale', 'prodotti_nome', 'prodotti_id_esterno']

    #preprocessing
    #fill null value to 0
    # product_template_ilaria_df["unita_organizzativa"] = product_template_ilaria_df["unita_organizzativa"].fillna(0)
    #
    # # convert in string
    # product_template_ilaria_df['codice_regionale_numerico'] = product_template_ilaria_df.codice_regionale_numerico.astype(str)
    # product_template_ilaria_df['unita_organizzativa'] = product_template_ilaria_df.unita_organizzativa.astype(str)
    # product_template_odoo_df['codice_numerico_regionale'] = product_template_odoo_df.codice_numerico_regionale.astype(str)
    # product_template_odoo_df['unita_organizzativa_nome'] = product_template_odoo_df.unita_organizzativa_nome.astype(str)
    #
    # product_template_odoo_df['unita_organizzativa_nome'] = product_template_odoo_df['unita_organizzativa_nome'].replace(['False'], '0')
    #
    # print("ilaria: " + product_template_ilaria_df.columns.values)
    # print("odoo " + product_template_odoo_df.columns.values)
    #
    # print("product_template_ilaria_df")
    # print(product_template_ilaria_df['unita_organizzativa'])
    # print("product_template_odoo_df")
    # print(product_template_odoo_df['unita_organizzativa_nome'])
    # Inner Join
    ## new_df = pd.merge(A_df, B_df,  how='left', left_on=['A_c1','c2'], right_on = ['B_c1','c2'])
    ## inner_join_df = customers.merge(calls, how="inner", on="Name")

    listino_generali_df["CodRegionaleNum"] = listino_generali_df["CodRegionaleNum"].fillna(0)
    listino_unisalute_df["CodRegionaleNum"] = listino_unisalute_df["CodRegionaleNum"].fillna(0)

    listino_generali_df['CodRegionaleNum'] = listino_generali_df.CodRegionaleNum.astype(int)
    listino_unisalute_df['CodRegionaleNum'] = listino_unisalute_df.CodRegionaleNum.astype(int)

    print(elenco_prodotti_id_df)
    print(listino_generali_df)
    print(listino_unisalute_df)

    elenco_prodotti_id_df['codice_regionale_numerico'] = elenco_prodotti_id_df.codice_regionale_numerico.astype(str)

    listino_generali_df['CodRegionaleNum'] = listino_generali_df.CodRegionaleNum.astype(str)
    listino_unisalute_df['CodRegionaleNum'] = listino_unisalute_df.CodRegionaleNum.astype(str)

    print(elenco_prodotti_id_df)
    print(listino_generali_df)
    print(listino_unisalute_df)

    inner_join_listino_generali_df = pd.merge(listino_generali_df, elenco_prodotti_id_df, how='left', left_on='CodRegionaleNum', right_on='codice_regionale_numerico')
    inner_join_listino_unisalute_df = pd.merge(listino_unisalute_df, elenco_prodotti_id_df, how='left', left_on='CodRegionaleNum', right_on='codice_regionale_numerico')

    inner_join_listino_generali_df.to_excel("destination/listino_generali_prodotti_id_df.xls")
    inner_join_listino_unisalute_df.to_excel("destination/listino_unisalute_prodotti_id_df.xls")