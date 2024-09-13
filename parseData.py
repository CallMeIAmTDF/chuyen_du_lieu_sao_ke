import re
import pdfplumber
import pandas as pd
date_pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
date_pattern2 = re.compile(r'^\d{2}/\d{2}/\d{4}\n$')
l_detail = []
l_credit = []
l_date = []
l_no = []
for i in range(1, 32):
    print(f"Load pdf_{i}")
    pdf_file = f"./pdfs/data{i}.pdf"
    with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                with open("output.txt", "w", encoding="utf-8") as txt_file:
                    txt_file.write(page.extract_text())
                clusters = []
                current_cluster = []
                txt_file = open("output.txt", "r", encoding="utf-8")
                element_to_remove = "Postal address: Telex : (0805) 411504 VCB - VT\n"
                lines = txt_file.readlines()
                data = lines[:lines.index(element_to_remove)] if element_to_remove in lines else lines
                element_to_remove = "Số CT/ Doc No\n"
                data = data[data.index(element_to_remove) + 1:] if element_to_remove in data else data
                for line in data:
                    line = line.strip().replace("\n", "")
                    if line:
                        if date_pattern.match(line) or date_pattern2.match(line):
                            if current_cluster:
                                clusters.append("\n".join(current_cluster))
                                current_cluster = []
                        current_cluster.append(line)
                if current_cluster:
                    clusters.append("\n".join(current_cluster))
                for d in clusters:
                    t = d.split("\n")
                    date = t[0]
                    no = t[2]
                    credit = t[1].split(" ")[0]
                    detail_footer = ' '.join(t[3:])
                    detail = ' '.join(t[1].split(" ")[1:]) + " " + detail_footer
                    l_detail.append(detail)
                    l_date.append(date)
                    l_no.append(no)
                    l_credit.append(credit)
df = pd.DataFrame({
    "date": l_date,
    "no": l_no,
    "credit": l_credit,
    "detail": l_detail
})
df.to_csv("./csv/data_1_31.csv", index=False)
                    # print({
                    #     'date': date,
                    #     'no': no,
                #     'credit': credit,
                #     'detail': detail
                # })
