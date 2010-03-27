python << end
import vim
(row, col) = vim.current.window.cursor
line = vim.current.buffer[row-1]
prevChar, nextChar = line[col-1], line[col]
end
