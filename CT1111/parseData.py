import re
import pdfplumber
import pandas as pd
date_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
date_pattern2 = re.compile(r'^\d{2}/\d{2}/\d{4}\n$')
l_detail = []
l_credit = []
l_date = []
l_no = []
l_page = []
count = 1
with pdfplumber.open("./CT1111.pdf") as pdf:
    for page in pdf.pages:
        print(count)
        rows = page.extract_table()
        for row in rows:
            l_detail.append(' '.join(row[2].split('\n')) + " | " + row[4].replace("\n", "").replace("\t", "").replace("- A/C",""))
            l_credit.append(row[3].replace('.', ''))
            l_date.append(row[1].split('\n')[0])
            l_no.append('')
            l_page.append(count)
        count = count + 1
df = pd.DataFrame({
    "date": l_date,
    "ct_num": l_no,
    "money": l_credit,
    "desc": l_detail,
    "page": l_page
})
df.to_csv("./CT.csv", index=False)