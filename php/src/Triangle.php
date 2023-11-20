<?php
declare(strict_types=1);

namespace Zim32\Php;

class Triangle extends BaseFigure
{
    private readonly int $sizeA;
    private readonly int $sizeB;
    private readonly int $sizeC;

    public function __construct(string $type, int $sizeA, int $sizeB, int $sizeC)
    {
        parent::__construct($type);
        $this->sizeA = $sizeA;
        $this->sizeB = $sizeB;
        $this->sizeC = $sizeC;
    }

    function computeArea(): float
    {
        $s = ($this->sizeA + $this->sizeB + $this->sizeC) / 2;
        return sqrt($s * ($s - $this->sizeA) * ($s - $this->sizeB) * ($s - $this->sizeC));
    }
}
