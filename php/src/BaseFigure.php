<?php
declare(strict_types=1);

namespace Zim32\Php;

abstract class BaseFigure implements FigureInterface
{
    private readonly string $type;

    public function __construct(string $type)
    {
        $this->type = $type;
    }

    public function getType(): string
    {
        return $this->type;
    }
}
