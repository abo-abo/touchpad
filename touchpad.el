;;; cook.el --- An Elisp wrapper for Python touchpad -*- lexical-binding: t -*-

;; Copyright (C) 2017 Oleh Krehel

;; Author: Oleh Krehel <ohwoeowho@gmail.com>
;; URL: https://github.com/abo-abo/touchpad
;; Version: 0.1.0
;; Keywords: touchpad, convenience

;; This file is not part of GNU Emacs

;; This file is free software; you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation; either version 3, or (at your option)
;; any later version.

;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.

;; For a full copy of the GNU General Public License
;; see <http://www.gnu.org/licenses/>.

;;;###autoload
(defun toggle-touchpad ()
  (interactive)
  (let ((cmd "tt"))
    (cond ((not (executable-find "tt"))
           (error "Install touchpad with: pip3 install touchpad"))
          ((not (executable-find "xinput"))
           (error "Install xinput with: apt-get install xinput"))
          (t
           (start-process-shell-command
            cmd nil
            (concat "nohup 1>/dev/null 2>/dev/null " cmd))))))

(provide 'touchpad)
