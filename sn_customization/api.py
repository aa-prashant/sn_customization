import frappe


@frappe.whitelist()
def update_serial_no():
    serial_no_list = [
        '0201200V000DH0200211',
        '0201200V000DH0200212',
        '0201200V000DH0200213',
        '0201200V000DH0200214',
        '0201200V000DH0200215',
        '0201200V000DH0200216',
        '0201200V000DH0200217',
        '0201200V000DH0200218',
        '0201200V000DH0200219',
        '0201200V000DI1501543',
        '0201200V000DI1501544',
        '0201200V000DI1501545',
        '0201200V000DI1501546',
        '0201200V000DI1501547',
        '0201200V000DI1501548',
        '0201200V000DI1501549',
        '0201200V000DI1501550',
        '0201200V000DI1501551',
        '0201200V000DI1501552',
        '0201200V000DI1501553',
        '0201200V000DI1501554',
        '0201200V000DI1501555',
        '0201200V000DI1501556'
    ]
    for row in serial_no_list:
        frappe.db.sql("""UPDATE `tabSerial No`
SET purchase_document_type='Stock Entry',
    purchase_document_no='MAT-STE-2022-00140',
    purchase_date='2022-10-01',
    purchase_time='16:13:06',
    purchase_rate='227.55',
    supplier='',
    supplier_name=''
WHERE name=%s""", str(row))


def update_serial_no_document_wise(doctype, name, item_code):
    document_details = frappe.get_doc(doctype, name)
    for row in document_details.items:
        if row.item_code == item_code:
            for s_row in row.serial_no.split("\n"):
                print(s_row)
                if frappe.db.exists("Serial No", s_row):
                    s_doc = frappe.get_doc("Serial No", s_row)
                    if not s_doc.purchase_document_no:
                        print('updated Serial No')
                        print(s_row)
                        if doctype == "Stock Entry":
                            row.rate = row.basic_rate
                        frappe.db.sql("""UPDATE `tabSerial No`
SET purchase_document_type=%s,
    purchase_document_no=%s,
    purchase_date=%s,
    purchase_time=%s,
    purchase_rate=%s
WHERE name=%s""", (
                            document_details.doctype, document_details.name, document_details.posting_date, document_details.posting_time, row.rate, s_row))
                else:
                    print(f"Serial No not exists {s_row}")


@frappe.whitelist()
def update_sn():
    update_serial_no()
    print("starting first")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00043", "AW-CSD381")
    print("ending first")
    print("Starting second")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00044", "AW-CFP2166-04C")
    print("ending second")
    print("Starting third")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00004", "AW-CSS2166-2")
    print("ending third")
    print("Starting fourth")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-CTD382")
    print("ending fourth")
    print("Starting fifth")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00153", "AW-D135C")
    print("ending fifth")
    print("Starting six")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00019", "AW-CSD311")
    print("ending six")
    print("Starting 7")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00022", "AW-CMC2166-06")
    print("ending 7")
    print("Starting 8")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00155", "AW-D135C")
    print("ending 8")
    print("Starting 9")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-CTD321")
    print("ending 9")
    print("Starting 10")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-CTD382")
    print("ending 10")
    print("Starting 10")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00155", "AW-D135C")
    print("ending 10")
    print("Starting 11")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-D135C")
    print("ending 11")
    print("Starting 12")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-D101")
    print("ending 12")
    print("Starting 13")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00044", "AW-CFP2166-02C")
    print("ending 13")
    print("Starting 14")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-SSD606D")
    print("ending 14")
    print("Starting 15")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00022", "AW-CMC2166-06")
    print("ending 15")
    print("Starting 15")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00022", "AW-CSD381")
    print("ending 15")
    print("Starting 16")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00022", "AW-CSD311")
    print("ending 16")
    print("Starting 17")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00022", "AW-CSD311")
    print("ending 17")
    print("Starting 18")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00043", "AW-CRP2166-GSM")
    print("ending 18")
    print("Starting 19")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-D106")
    print("ending 19")
    print("Starting 20")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-D105")
    print("ending 20")
    print("Starting 21")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-CTD382")
    print("ending 21")
    print("Starting 22")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00043", "AW-D111")
    print("ending 22")
    print("Starting 23")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-CBL2166-08")
    print("ending 23")
    print("Starting 24")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-D102")
    print("ending 24")
    print("Starting 25")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00022", "AW-CBL2166-06")
    print("ending 25")
    print("Starting 26")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00013", "AW-CSD311")
    print("ending 26")

    print("Starting 27")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00153", "AW-D135C")
    print("ending 27")

    print("Starting 28")
    update_serial_no_document_wise(
        "Purchase Receipt", "MAT-PRE-2022-00043", "AW-CSD381")
    print("ending 28")

    print("Starting 29")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-CTD321")
    print("ending 29")

    print("Starting 30")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00140", "AW-CTD321")
    print("ending 30")
    print("Starting 31")
    update_serial_no_document_wise(
        "Stock Entry", "MAT-STE-2022-00153", "AW-D135C")
    print("ending 31")
