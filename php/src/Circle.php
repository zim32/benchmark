<?php
declare(strict_types=1);

namespace Zim32\Php;

class Circle extends BaseFigure
{
    private readonly int $diameter;

    public function __construct(string $type, int $diameter)
    {
        parent::__construct($type);
        $this->diameter = $diameter;
    }

    function computeArea(): float
    {
        $radius = $this->diameter / 2;
        return M_PI * pow($radius, 2);
    }
}
