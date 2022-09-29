const path = require('path');
const express = require("express");
const bodyParser = require('body-parser');
const ejs = require('ejs');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true}));

app.get('/', (req, res) => res.render('main_dp')); //메인화면

app.listen(port, () => console.log("listening"));

const mysql = require('mysql');
const res = require('express/lib/response');

const con = mysql.createConnection({
    host: 'localhost',
	user: 'root',
	password: 'password',
	db: 'librarydb'
});

con.connect(function(err){
    if(err) throw err;
    console.log("Connected");
});

//회원 등록
app.get('/sign_up', (req, res) => {
        res.render('sign_up');
});

app.post('/sign_up', (req, res)=> {
    const sql_check1 = "select * from librarydb.userinfo where ID = ?";
    con.query(sql_check1, [req.body.id] ,function(err, result, fields){
        if (err) throw err;
        if (result.length != 0){
            res.send("<script>alert('중복된 ID 입니다. 다시 입력해주십시오.'); location.href='/sign_up';</script>");
        }
        else{
            const sql = "INSERT INTO librarydb.userInfo VALUES (?, ?, ?, 5);";
            //5권씩 기본으로 빌릴 수 있게 함.
            con.query(sql,[req.body.id, req.body.name, req.body.phonenum] ,function(err, result, fields){
            if (err) throw err;
            res.send("<script>alert('등록 성공!'); location.href='/sign_up';</script>");
            });
        }
    });
});

//책 검색
app.get('/research', (req, res) => {
    var search_val = "nothing";
    var sql = "SELECT title, author, lname, qty FROM librarydb.book, librarydb.library, librarydb.connect WHERE book.title like '%"
        +search_val+"%' AND book.bcode = connect.bookcode AND library.lcode = connect.libcode"
    con.query(sql, [req.body.search], function(err, result, fields){
        if (err) throw err;
        res.render('research', {results:result});
    });
});

app.post('/research', (req, res)=> {
    var selectOption = req.body.sel;
    var search_val = req.body.search;
    search_val = search_val.replace("'",'');
    if(selectOption == "title"){
        var sql = "SELECT title, author, lname, qty FROM librarydb.book, librarydb.library, librarydb.connect WHERE book.title like '%"
        +search_val+"%' AND book.bcode = connect.bookcode AND library.lcode = connect.libcode"
    } else if(selectOption == "author"){
        var sql = "SELECT title, author, lname, qty FROM librarydb.book, librarydb.library, librarydb.connect WHERE book.author like '%"
        +search_val+"%' AND book.bcode = connect.bookcode AND library.lcode = connect.libcode"
    }
    con.query(sql, function(err, result, fields){
        if (err) throw err;
        res.render('research', {results:result});
    });
});

//도서관 검색
app.get('/libsearch', (req, res) => {
    var search = "nothing";
    const sql = "select lname, location, title, author, qty from librarydb.library, librarydb.book, librarydb.connect where lname like '%"
    +search+"%' and library.lcode = connect.libcode and book.bcode = connect.bookcode;";
    con.query(sql, function(err, result, fields){
        if (err) throw err;
        res.render('libsearch', {results:result});
    });
});

app.post('/libsearch', (req, res)=> {
    var search = req.body.libsearch;
    search = search.replace("'",'');
    const sql = "select lname, location, title, author, qty from librarydb.library, librarydb.book, librarydb.connect where lname like '%"
    +search+"%' and library.lcode = connect.libcode and book.bcode = connect.bookcode;";
    con.query(sql, function(err, result, fields){
        if (err) throw err;
        res.render('libsearch', {results:result});
    });
});

//내 정보 확인
app.get('/myinfo', (req, res) => {
    var ID = "nothing";
    var PHONENUM = "nothing";
    const sql = "select * from librarydb.userinfo where ID = '"
    +ID+"' and PHONENUM like '______"+PHONENUM+"'";
    con.query(sql, function(err, result, fields){
        if (err) throw err;
        res.render('myinfo', {results:result});
    });
});

app.post('/myinfo', (req, res)=> {
    var ID = req.body.id;
    var PHONENUM = req.body.num;
    const sql = "select * from librarydb.userinfo where ID = '"
    +ID+"' and PHONENUM like '_______"+PHONENUM+"'";
    con.query(sql, function(err, result, fields){
        if (err) throw err;
        if (result.length == 0){
            res.send("<script>alert('해당하는 회원의 정보가 존재하지 않습니다.'); location.href='/myinfo';</script>");
        }else{
            res.render('myinfo', {results:result});
        }
    });
});