
fr_domain = [("Plafond", "Ceiling"),("Équipement", "Equipments"),("Électricité", "Electricity"), ("Maçonnerie", "Masonry"), ("Plomberie", "Plumbing"), ("Peinture", "Painting"), ("Échafaudage", "Scaffolding"), ("Carrelage", "Tiling"), ("Etancheite", "Waterproofing"), ("Autres", "Others")]

fr_report = [("Registres d'Entrée", "Entry Records"), ("Registres des Sorti", "Exit Records"), ("Grand Livre", "Ledger Records"), ("Niveau de stock actuel", "Current Stock Level")]



def french(entry, exit_sec, stock, report):
    """This function translates all Labels, buttons and radiobuttons to French"""

    ###########--------ENTRY SECTION------########
    entry.entry_label.config(text="ENTREE")
    entry.domain_label.config(text="Domaine")
    entry.item_label.config(text="Matériel")
    entry.units_label.config(text="Unité")
    entry.qty_label.config(text="Qté")
    entry.search_item_btn.config(text="cliquez ici si le matériel s'il est déjà en stock")
    entry.entry_cancel_btn.config(text="Annuler la transaction")
    entry.validate_entry_btn.config(text="Valider l'entrée")
    entry.select_btn.config(text="Sélectionner")
    entry.cancel_btn.config(text="Annuler")

    for i in range(len(entry.radio_b_list)):
        entry.radio_b_list[i].config(text=fr_domain[i][0])


    ###########--------EXIT SECTION------########
    exit_sec.exit_label.config(text="SORTIE")
    exit_sec.exit_material_label.config(text="Matériel")
    exit_sec.exit_mat_cat_label.config(text="Domaine")
    exit_sec.material_unit_label.config(text="Unité")
    exit_sec.exit_current_qty_label.config(text="Qté actuel")
    exit_sec.exit_qty_label.config(text="Qté Sortant")
    exit_sec.material_exit_description.config(text="Entrez une description concise du travail à effectuer avec ce matériau")
    exit_sec.exit_search_item_btn.config(text="cliquez ici pour sélectionner le matériel")
    exit_sec.exit_cancel_btn.config(text="Annuler la transaction")
    exit_sec.validate_exit_btn.config(text="Valider l'entrée")
    exit_sec.select_btn.config(text="Sélectionner")
    exit_sec.cancel_btn.config(text="Annuler")

    ##############--------STOCK CHECK------########
    stock.check_label.config(text="Vérification des stocks")
    stock.check_domain.config(text="Domaine")
    stock.check_qty.config(text="Qté en stock")
    stock.select_btn3.config(text="Sélect")
    stock.select_btn4.config(text="Effacer")


    ##############--------REPORT------###########
    for i in range(len(report.rb_list)):
        report.rb_list[i].config(text=fr_report[i][0])

    report.gen_excel_btn.config(text="EXPORTER DES ENREGISTREMENTS VERS MICROSOFT EXCEL")




def english(entry, exit_sec, stock, report):
    """This function translates all Labels, buttons and radiobuttons to English"""

    ###########--------ENTRY SECTION------########
    entry.entry_label.config(text="ENTRY")
    entry.domain_label.config(text="Domain")
    entry.item_label.config(text="Material")
    entry.units_label.config(text="Unit")
    entry.qty_label.config(text="Qty")
    entry.search_item_btn.config(text="click here to select material if already in stock")
    entry.entry_cancel_btn.config(text="Cancel transaction")
    entry.validate_entry_btn.config(text="Validate Entry")
    entry.select_btn.config(text="Select")
    entry.cancel_btn.config(text="Cancel")

    for i in range(len(entry.radio_b_list)):
        entry.radio_b_list[i].config(text=fr_domain[i][1])   


    ###########--------EXIT SECTION------########
    exit_sec.exit_label.config(text="EXIT")
    exit_sec.exit_material_label.config(text="Material")
    exit_sec.exit_mat_cat_label.config(text="Domain")
    exit_sec.material_unit_label.config(text="Unit")
    exit_sec.exit_current_qty_label.config(text="Current Qty")
    exit_sec.exit_qty_label.config(text="Exit Qty")
    exit_sec.material_exit_description.config(text="Enter a concise description of the work to be done with this material:")
    exit_sec.exit_search_item_btn.config(text="click here to select material from stock")
    exit_sec.exit_cancel_btn.config(text="Cancel transaction")
    exit_sec.validate_exit_btn.config(text="Validate Exit")
    exit_sec.select_btn.config(text="Select")
    exit_sec.cancel_btn.config(text="Cancel")

    ##############--------STOCK CHECK------########
    stock.check_label.config(text="Stock Check")
    stock.check_domain.config(text="Domain")
    stock.check_qty.config(text="Quantity in stock:")
    stock.select_btn3.config(text="Select")
    stock.select_btn4.config(text="Clear")


    ##############--------REPORT------###########
    for i in range(len(report.rb_list)):
        report.rb_list[i].config(text=fr_report[i][1])
        
    report.gen_excel_btn.config(text="EXPORT RECORDS TO MICROSOFT EXCEL")
