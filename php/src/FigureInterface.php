<?php

declare(strict_types=1);

namespace Zim32\Php;

interface FigureInterface
{
    function computeArea(): float;

    function getType(): string;
}
