<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $kodeBuku = "";
    public $judul = "";
    public $kodeKategori = "";
    public $penulis = "";
    public $penerbit = "";
    public $tahun = "";
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
    public function get_by_kodeBuku(string $kodeBuku)
    {
        $query = "SELECT * FROM $this->table WHERE kodeBuku = '$kodeBuku'";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodeBuku`,`judul`,`kodeKategori`,`penulis`,`penerbit`,`tahun`) VALUES ('$this->kodeBuku','$this->judul','$this->kodeKategori','$this->penulis','$this->penerbit','$this->tahun')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodeBuku = '$this->kodeBuku', judul = '$this->judul', kodeKategori = '$this->kodeKategori', penulis = '$this->penulis', penerbit = '$this->penerbit', tahun = '$this->tahun' 
        WHERE idBuku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodeBuku(string $kodeBuku): int
    {
        $query = "UPDATE $this->table SET kodeBuku = '$this->kodeBuku', judul = '$this->judul', kodeKategori = '$this->kodeKategori', penulis = '$this->penulis', penerbit = '$this->penerbit', tahun = '$this->tahun' 
        WHERE kodeBuku = '$kodeBuku'";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idBuku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodeBuku($kodeBuku): int
    {
        $query = "DELETE FROM $this->table WHERE kodeBuku = $kodeBuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>