<?php
for ($x = 0; $x <= 100; $x++) {
    for ($y = 0; $y <= 100; $y++) {
        if ((100 - $x - $y) % 3 === 0 && 5 * $x + $y * 3 + (100 - $x - $y)/3 === 100) {
            printf('鸡翁: %d, 鸡母: %d, 鸡雏: %d'."\n", $x, $y, 100 - $x -$y);
        }
    }
}