<?php
//Simpanlah dengan nama file : Kategori.php
require_once 'database.php';
class Kategori 
{
    private $db;
    private $table = 'kategori';
    public $kodeKategori = "";
    public $namaKategori = "";
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
    public function get_by_kodeKategori(string $kodeKategori)
    {
        $query = "SELECT * FROM $this->table WHERE kodeKategori = '$kodeKategori'";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodeKategori`,`namaKategori`) VALUES ('$this->kodeKategori','$this->namaKategori')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodeKategori = '$this->kodeKategori', namaKategori = '$this->namaKategori' 
        WHERE idKategori = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodeKategori(string $kodeKategori): int
    {
        $query = "UPDATE $this->table SET kodeKategori = '$this->kodeKategori', namaKategori = '$this->namaKategori' 
        WHERE kodeKategori = '$kodeKategori'";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idKategori = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodeKategori(string $kodeKategori): int
    {
        $query = "DELETE FROM $this->table WHERE kodeKategori = '$kodeKategori'";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>