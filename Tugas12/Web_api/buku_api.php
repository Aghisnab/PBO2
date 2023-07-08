<?php
require_once 'database.php';
require_once 'Buku.php';
$db = new MySQLDatabase();
$buku = new Buku($db);
$id=0;
$kodeBuku=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodeBuku'])){
            $kodeBuku = $_GET['kodeBuku'];
        }
        if($id>0){    
            $result = $buku->get_by_id($id);
        }elseif($kodeBuku>0){
            $result = $buku->get_by_kodeBuku($kodeBuku);
        } else {
            $result = $buku->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new buku
        $buku->kodeBuku = $_POST['kodeBuku'];
        $buku->judul = $_POST['judul'];
        $buku->kodeKategori = $_POST['kodeKategori'];
        $buku->penulis = $_POST['penulis'];
        $buku->penerbit = $_POST['penerbit'];
        $buku->tahun = $_POST['tahun'];
       
        $buku->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodeBuku'])){
            $kodeBuku = $_GET['kodeBuku'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $buku->kodeBuku = $_PUT['kodeBuku'];
        $buku->judul = $_PUT['judul'];
        $buku->kodeKategori = $_PUT['kodeKategori'];
        $buku->penulis = $_PUT['penulis'];
        $buku->penerbit = $_PUT['penerbit'];
        $buku->tahun = $_PUT['tahun'];
        if($id>0){    
            $buku->update($id);
        }elseif($kodeBuku<>""){
            $buku->update_by_kodeBuku($kodeBuku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodeBuku'])){
            $kodeBuku = $_GET['kodeBuku'];
        }
        if($id>0){    
            $buku->delete($id);
        }elseif($kodeBuku>0){
            $buku->delete_by_kodeBuku($kodeBuku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>