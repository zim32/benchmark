<?php
declare(strict_types=1);

namespace Zim32\Php;

class Rectangle extends BaseFigure
{
    private readonly int $sizeA;
    private readonly int $sizeB;

    public function __construct(string $type, int $sizeA, int $sizeB)
    {
        parent::__construct($type);
        $this->sizeA = $sizeA;
        $this->sizeB = $sizeB;
    }

    function computeArea(): float
    {
        return $this->sizeA * $this->sizeB;
    }
}
