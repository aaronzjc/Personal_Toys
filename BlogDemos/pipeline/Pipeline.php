<?php

class Pipeline {
    private $stages = [];
    private $processor;

    public function __construct($stages = [], ProcessInterface $processor = NULL) {
        foreach ($stages as $stage) {
            if (!is_callable($stage)) {
                throw new InvalidArgumentException('流水线必须可访问');
            }
        }

        $this->stages = $stages;
        $this->processor = $processor?:new DefaultProcessor();
    }

    public function pipe(callable $stage) {
        $this->stages[] = $stage;

        return $this;
    }

    public function process($payload) {
        return $this->processor->process($this->stages, $payload);
    }

    public function __invoke($payload) {
        return $this->process($payload);
    }
}