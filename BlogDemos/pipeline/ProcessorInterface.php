<?php
interface ProcessorInterface {
    public function process($stages, $payload);
}