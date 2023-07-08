<?php
//Simpanlah dengan nama file : Pinjam.php
require_once 'database.php';
class Pinjam 
{
    private $db;
    private $table = 'pinjam';
    public $kodePinjam = "";
    public $kodeAnggota = "";
    public $kodeBuku = "";
    public $tglKembali = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kodePinjam(int $kodePinjam)
    {
        $query = "SELECT * FROM $this->table WHERE kodePinjam = $kodePinjam";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodePinjam`,`kodeAnggota`,`kodeBuku`,`tglKembali`) VALUES ('$this->kodePinjam','$this->kodeAnggota','$this->kodeBuku','$this->tglKembali')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodePinjam = '$this->kodePinjam', kodeAnggota = '$this->kodeAnggota', kodeBuku = '$this->kodeBuku', tglKembali = '$this->tglKembali' 
        WHERE idPinjam = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodePinjam($kodePinjam): int
    {
        $query = "UPDATE $this->table SET kodePinjam = '$this->kodePinjam', kodeAnggota = '$this->kodeAnggota', kodeBuku = '$this->kodeBuku', tglKembali = '$this->tglKembali' 
        WHERE kodePinjam = $kodePinjam";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idPinjam = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodePinjam($kodePinjam): int
    {
        $query = "DELETE FROM $this->table WHERE kodePinjam = $kodePinjam";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>