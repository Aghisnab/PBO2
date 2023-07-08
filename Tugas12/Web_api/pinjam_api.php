<?php
require_once 'database.php';
require_once 'Pinjam.php';
$db = new MySQLDatabase();
$pinjam = new Pinjam($db);
$id=0;
$kodePinjam=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodePinjam'])){
            $kodePinjam = $_GET['kodePinjam'];
        }
        if($id>0){    
            $result = $pinjam->get_by_id($id);
        }elseif($kodePinjam>0){
            $result = $pinjam->get_by_kodePinjam($kodePinjam);
        } else {
            $result = $pinjam->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pinjam
        $pinjam->kodePinjam = $_POST['kodePinjam'];
        $pinjam->kodeAnggota = $_POST['kodeAnggota'];
        $pinjam->kodeBuku = $_POST['kodeBuku'];
        $pinjam->tglKembali = $_POST['tglKembali'];
       
        $pinjam->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pinjam created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pinjam not created.';
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
        if(isset($_GET['kodePinjam'])){
            $kodePinjam = $_GET['kodePinjam'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $pinjam->kodePinjam = $_PUT['kodePinjam'];
        $pinjam->kodeAnggota = $_PUT['kodeAnggota'];
        $pinjam->kodeBuku = $_PUT['kodeBuku'];
        $pinjam->tglKembali = $_PUT['tglKembali'];
        if($id>0){    
            $pinjam->update($id);
        }elseif($kodePinjam<>""){
            $pinjam->update_by_kodePinjam($kodePinjam);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pinjam updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pinjam update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodePinjam'])){
            $kodePinjam = $_GET['kodePinjam'];
        }
        if($id>0){    
            $pinjam->delete($id);
        }elseif($kodePinjam>0){
            $pinjam->delete_by_kodePinjam($kodePinjam);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pinjam deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pinjam delete failed.';
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