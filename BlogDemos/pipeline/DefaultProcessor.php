<?php
class DefaultProcessor implements ProcessorInterface {
    public function process($stages, $payload) {
        foreach ($stages as $stage) {
            $payload = call_user_func($stage, $payload);
        }

        return $payload;
    }
}