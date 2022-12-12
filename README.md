*** Yêu cầu ***


  Làm tối thiểu 3 bài GUI tkinter python
  Làm tối thiểu 3 câu trong Bài tập MySql (có tất cả 8 câu) và làm một trang web streamlit python cho 3 câu này
  Xong nén tất cả vào một file .zip hay .rar và nộp vào đây.

* Cách cài mysql trên ubuntu:

	https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/#repo-qg-apt-upgrading
	
	
* Mật khẩu cho mysql server root account: rootpw

* Đăng nhập: mysql -h localhost -u root -p

* Tải workbench: sudo snap install mysql-workbench-community

* Kích hoạt local infile: set global local_infile=true;
  1. Stackoverflow: https://stackoverflow.com/questions/59993844/error-loading-local-data-is-disabled-this-must-be-enabled-on-both-the-client/62965185#62965185

* Sau đó exit mysql với lệnh exit

* Đăng nhập lại: mysql --local-infile=1 -h localhost -u root -p

* Cách sử dụng môi trường ảo python venv (standard) trên ubuntu linux

        Tạo folder chứa môi trường ảo, đặt tên, ví dụ: myenv
        Tái: sudo apt-get install python3.x-venv (x là phiên bản python 3)
        Kích hoạt môi trường(trên bash - chú ý nhớ thoát ra folder cha):
            a. python3 -m venv myenv
            b. source myenv/bin/activate

* Tải official mysql client:

    $> pip install mysql-connector-python

* Uncomment code block: ctrl k u

* Tải streamlit: pip install streamlit

* Chạy streamlit: streamlit run <filename>.py

* Cách tới và cách lùi nhiều dòng trong python: Chọn block of code


    1. Tới là Tab
    2. Lùi là shift - tab

* Clear trên mysql terminal trong linux: ctrl l