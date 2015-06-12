<?php
namespace PhotoBasket;

define('LAZER_DATA_PATH', __DIR__.'/../../db/data/'); //Path to folder with tables
use Lazer\Classes\Database as Lazer;

class DB {
    public function __construct() {
        $this->check_database();
    }

    public static function get_album($album_ident) {
        new DB();
        $result = Lazer::table('albums')->where('ident', '=', $album_ident)
                                        ->find()
                                        ->asArray();
        if ($result && $result[0]) {
            return $result[0];
        }
    }

    public static function get_album_user($album_ident, $user_key) {
        new DB();
        $result = Lazer::table('users')->where('album_ident', '=', $album_ident)
                                        ->andWhere('key', '=', $user_key)
                                        ->find()
                                        ->asArray();
        if ($result && $result[0]) {
            return $result[0];
        }
    }

    public static function get_album_users($album_ident) {
        new DB();
        $result = Lazer::table('users')->where('album_ident', '=', $album_ident)
                                        ->findAll()
                                        ->asArray();
        if ($result && $result[0]) {
            return $result;
        }
    }

    public static function get_album_images($album_ident) {
        new DB();
        $result = Lazer::table('images')->where('album_ident', '=', $album_ident)
                                        ->findAll()
                                        ->asArray();
        if ($result && $result[0]) {
            return $result;
        }
    }

    public static function create_album_user($album_ident, $user_email) {
        new DB();

        if (count(DB::get_album_user($album_ident, $user_email)) >= 1) {
            throw new Exception('Division durch Null.');
        }

        $uniqid = uniqid('', true);
        $uniqid = str_replace('.', '', $uniqid);
        $uniqid = substr($uniqid, 0, 15);

        $row = Lazer::table('users');
        $row->album_ident = $album_ident;
        $row->email = $user_email;
        $row->key = $uniqid;
        $row->save();

        return $uniqid;
    }

    protected function check_database() {
        try{
            \Lazer\Classes\Helpers\Validate::table('albums')->exists();
        } catch(\Lazer\Classes\LazerException $e){
            $this->create_table_albums();
        }

        try{
            \Lazer\Classes\Helpers\Validate::table('users')->exists();
        } catch(\Lazer\Classes\LazerException $e){
            $this->create_table_users();
        }

        try{
            \Lazer\Classes\Helpers\Validate::table('images')->exists();
        } catch(\Lazer\Classes\LazerException $e){
            $this->create_table_images();
        }
    }

    protected function create_table_albums() {
        Lazer::create('albums', array(
            'name'          => 'string',
            'ident'         => 'string',
            'description'   => 'string',
            'soundcloud_url'=> 'string'
        ));
    }

    protected function create_table_users() {
        Lazer::create('users', array(
            'album_ident'   => 'string',
            'email'         => 'string',
            'key'           => 'string'
        ));
    }

    protected function create_table_images() {
        Lazer::create('images', array(
            'album_ident'   => 'string',
            'user_key'      => 'string',
            'path'          => 'string',
            'size'          => 'string'
        ));
    }
}