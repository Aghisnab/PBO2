<?php
require_once 'database.php';
require_once 'Kembali.php';
$db = new MySQLDatabase();
$kembali = new Kembali($db);
$id=0;
$kodeKembali=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodeKembali'])){
            $kodeKembali = $_GET['kodeKembali'];
        }
        if($id>0){    
            $result = $kembali->get_by_id($id);
        }elseif($kodeKembali>0){
            $result = $kembali->get_by_kodeKembali($kodeKembali);
        } else {
            $result = $kembali->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new kembali
        $kembali->kodeKembali = $_POST['kodeKembali'];
        $kembali->kodeAnggota = $_POST['kodeAnggota'];
        $kembali->kodePinjam = $_POST['kodePinjam'];
        $kembali->kodeBuku = $_POST['kodeBuku'];
        $kembali->tglDikembalikan = $_POST['tglDikembalikan'];
        $kembali->denda = $_POST['denda'];
       
        $kembali->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kembali created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kembali not created.';
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
        if(isset($_GET['kodeKembali'])){
            $kodeKembali = $_GET['kodeKembali'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $kembali->kodeKembali = $_PUT['kodeKembali'];
        $kembali->kodeAnggota = $_PUT['kodeAnggota'];
        $kembali->kodePinjam = $_PUT['kodePinjam'];
        $kembali->kodeBuku = $_PUT['kodeBuku'];
        $kembali->tglDikembalikan = $_PUT['tglDikembalikan'];
        $kembali->denda = $_PUT['denda'];
        if($id>0){    
            $kembali->update($id);
        }elseif($kodeKembali<>""){
            $kembali->update_by_kodeKembali($kodeKembali);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kembali updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kembali update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodeKembali'])){
            $kodeKembali = $_GET['kodeKembali'];
        }
        if($id>0){    
            $kembali->delete($id);
        }elseif($kodeKembali>0){
            $kembali->delete_by_kodeKembali($kodeKembali);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Kembali deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Kembali delete failed.';
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