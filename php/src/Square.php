<?php
declare(strict_types=1);

namespace Zim32\Php;

class Square extends BaseFigure
{
    private readonly int $size;

    public function __construct(string $type, int $size)
    {
        parent::__construct($type);
        $this->size = $size;
    }

    function computeArea(): float
    {
        return pow($this->size, 2);
    }
}
