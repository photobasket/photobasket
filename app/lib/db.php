<?php
namespace PhotoBasket;

define('LAZER_DATA_PATH', __DIR__.'/../../db/data/'); //Path to folder with tables
use Lazer\Classes\Database as Lazer;

class DB {
    public function __construct() {
        $this->check_database();
    }

    public static function get_album($ident) {
        new DB();
        return Lazer::table('albums')->where('ident', '=', $ident)->find()->asArray()[0];
    }

    protected function check_database() {
        try{
            \Lazer\Classes\Helpers\Validate::table('albums')->exists();
        } catch(\Lazer\Classes\LazerException $e){
            $this->create_table_albums();
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
}