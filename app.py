import mysql.connector
import streamlit as st
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password='rootpw',
                              host='localhost',
                              database='QuanLyDiemThi')
cursor = cnx.cursor()

st.title("Bài 1")

query = ("select * from ChiTietDT;")
cursor.execute(operation = query)


st.header("Xem bảng ChiTietDT")
for (doiTuongDT, dienGiaiDT, diemUT) in cursor:
#   Test    
#   print("{} {} {}".format(doiTuongDT, dienGiaiDT, diemUT))
    line: str = "{} {} {}".format(doiTuongDT, dienGiaiDT, diemUT)
    st.write(line)


del (doiTuongDT, dienGiaiDT, diemUT)


query = ("select * from DanhSach limit 10;")
cursor.execute(operation = query)


st.header("Xem bảng DanhSach")
for (sbd, ho, ten, phai, ngaySinh, dtDt) in cursor:


    line: str = "{} {} {} {} {} {}".format(sbd, ho, ten, phai, ngaySinh, dtDt)
    st.write(line)


del (sbd, ho, ten, phai, ngaySinh, dtDt)


query = ("select * from DanhSach limit 10;")
cursor.execute(operation = query)


st.header("Xem bảng DanhSach")
for (sbd, ho, ten, phai, ngaySinh, dtDt) in cursor:


    line: str = "{} {} {} {} {} {}".format(sbd, ho, ten, phai, ngaySinh, dtDt)
    st.write(line)


del (sbd, ho, ten, phai, ngaySinh, dtDt)

st.title("Bài 2")
with st.form("Nhập thông tin thí sinh"):


    sbd = int(st.number_input("Nhập số báo danh: "))
    ho = st.text_input("Nhập họ: ")


    ten = st.text_input("Nhập tên: ")
    phai = int(st.number_input("Nhập giới tính (0 là nam, 1 là nữ)"))


    ngaySinh = st.text_input("Nhập ngày sinh: ")
    dTdT = int(st.number_input("Nhập đối tượng dự thi (0 hoặc 1 hoặc 2 hoặc 3): "))

    submitted = st.form_submit_button("Xác nhận")
    if submitted:

       print("{} {} {} {} {} {}".format(sbd, ho, ten, phai, ngaySinh, dTdT))
       statement = (


        """INSERT INTO DanhSach(SBD, Ho, Ten, Phai, NgaySinh, DTDT)
           VALUES(%s, %s, %s, %s, STR_TO_DATE(%s, '%Y-%m-%d'), %s);"""


       )
       data = (sbd, ho, ten, phai, ngaySinh, dTdT)

       cursor.execute(statement, data)
       st.success("Đã nhập dữ liệu")

       cnx.commit()
       cursor.close()


with st.form("Nhập điểm thi của thí sinh"):


    sbd = int(st.number_input("Nhập số báo danh: "))
    toan = st.number_input("Nhập điểm Toán: ")


    van = st.number_input("Nhập điểm Văn: ")
    anh = st.number_input("Nhập điểm Anh: ")


    submitted = st.form_submit_button("Xác nhận")
    if submitted:

       print("{} {} {} {}".format(sbd, toan, van, anh))
       statement = (


        """INSERT INTO DiemThi(SBD, Toan, Van, AnhVan)
           VALUES(%s, %s, %s, %s);"""


       )
       data = (sbd, toan, van, anh)

       cursor.execute(statement, data)
       st.success("Đã nhập dữ liệu")

       cnx.commit()
       cursor.close()

st.title("Bài 3")
try:


    statement = """
        create table Tmp_DiemThiTongHop
            select 
                DanhSach.SBD, 
                DanhSach.Ho, 
                DanhSach.Ten, 
                DanhSach.Phai,
                DanhSach.NgaySinh,
                Toan,
                Van,
                AnhVan,
                DiemUT, 
                Least(Toan,Van,AnhVan) AS DTN, 
                Toan + Van + AnhVan + DiemUT As TongDiem
            from DanhSach
                left join ChiTietDT on DanhSach.DTDT = ChiTietDT.DoiTuongDT
                left join DiemThi on DanhSach.SBD = DiemThi.SBD
                order by SBD;
    """

    cursor.execute(statement)
except mysql.connector.Error as err:


    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")


    else:
            print(err.msg)


else:
    print("OK")


query = (
    """
        select 
            SBD, 
            Ho, 
            Ten, 
            Phai, 
            NgaySinh, 
            Toan, 
            Van, 
            AnhVan, 
            DiemUT, 
            DTN, 
            TongDiem, 
            IF(TongDiem >= 24 AND DTN >= 7,"Gioi",
            IF(TongDiem >= 21 AND DTN >= 6, "Kha",
            IF(TongDiem >= 15 AND DTN >= 4, "Trung binh", "Chua Dat"))) 
        As XepLoai from Tmp_DiemThiTongHop order by SBD limit 10;
    """
)


cursor.execute(query)
st.header("Kết quả")

for (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12) in cursor:
    line = "{} {} {} {} {} {} {} {} {} {} {} {}".format(
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12
    )
    st.write(line)


cursor.close()
cnx.close()