<?php
//Simpanlah dengan nama file : Anggota.php
require_once 'database.php';
class Anggota 
{
    private $db;
    private $table = 'anggota';
    public $kodeAnggota = "";
    public $nama = "";
    public $alamat = "";
    public $bergabung = "";
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
    public function get_by_kodeAnggota(int $kodeAnggota)
    {
        $query = "SELECT * FROM $this->table WHERE kodeAnggota = $kodeAnggota";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodeAnggota`,`nama`,`alamat`,`bergabung`) VALUES ('$this->kodeAnggota','$this->nama','$this->alamat','$this->bergabung')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodeAnggota = '$this->kodeAnggota', nama = '$this->nama', alamat = '$this->alamat', bergabung = '$this->bergabung' 
        WHERE idAnggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodeAnggota($kodeAnggota): int
    {
        $query = "UPDATE $this->table SET kodeAnggota = '$this->kodeAnggota', nama = '$this->nama', alamat = '$this->alamat', bergabung = '$this->bergabung' 
        WHERE kodeAnggota = $kodeAnggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idAnggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodeAnggota($kodeAnggota): int
    {
        $query = "DELETE FROM $this->table WHERE kodeAnggota = $kodeAnggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>