<?php
//Simpanlah dengan nama file : Kembali.php
require_once 'database.php';
class Kembali 
{
    private $db;
    private $table = 'kembali';
    public $kodeKembali = "";
    public $kodeAnggota = "";
    public $kodePinjam = "";
    public $kodeBuku = "";
    public $tglDikembalikan = "";
    public $denda = "";
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
    public function get_by_kodeKembali(int $kodeKembali)
    {
        $query = "SELECT * FROM $this->table WHERE kodeKembali = $kodeKembali";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodeKembali`,`kodeAnggota`,`kodePinjam`,`kodeBuku`,`tglDikembalikan`,`denda`) VALUES ('$this->kodeKembali','$this->kodeAnggota','$this->kodePinjam','$this->kodeBuku','$this->tglDikembalikan','$this->denda')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodeKembali = '$this->kodeKembali', kodeAnggota = '$this->kodeAnggota', kodePinjam = '$this->kodePinjam', kodeBuku = '$this->kodeBuku', tglDikembalikan = '$this->tglDikembalikan', denda = '$this->denda' 
        WHERE idKembali = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodeKembali($kodeKembali): int
    {
        $query = "UPDATE $this->table SET kodeKembali = '$this->kodeKembali', kodeAnggota = '$this->kodeAnggota', kodePinjam = '$this->kodePinjam', kodeBuku = '$this->kodeBuku', tglDikembalikan = '$this->tglDikembalikan', denda = '$this->denda' 
        WHERE kodeKembali = $kodeKembali";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idKembali = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodeKembali($kodeKembali): int
    {
        $query = "DELETE FROM $this->table WHERE kodeKembali = $kodeKembali";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>