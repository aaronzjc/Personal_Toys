<?php
spl_autoload_register();

$stageOne = function($payload) {
    return $payload * 10;
};

$stageTwo = function($payload) {
    return $payload + 1;
};


class Stage {
    public static function stageOne($payload) {
        return $payload . "->stageOne";
    }

    public static function stageTwo($payload) {
        return $payload . "->stageTwo";
    }
}

$pipeOne = new Pipeline();
$pipeOne->pipe($stageOne)->pipe($stageTwo);

$pipeline = new Pipeline();
$result = $pipeline->pipe($pipeOne)->pipe([Stage::class, "stageOne"])->pipe([Stage::class, "stageTwo"])->process(10);

echo $result;