# Colors
RED     := \033[0;31m
GREEN   := \033[0;32m
YELLOW  := \033[0;33m
BLUE    := \033[0;34m
PURPLE  := \033[0;35m
YELLOW2	:= \033[33;1m
CYAN    := \033[0;36m
RESET   := \033[0m
BOLD    := \033[1m

VENV = venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip
MAIN_SCRIPT := fly_in.py
CONFIG_FILE := config.txt

.PHONY: venv install run debug clean lint lint-strict help
.DEFAULT_GOAL := help

venv:
	@echo "$(YELLOW)$(BOLD)Creating virtual environment...$(RESET)"
	python3 -m venv $(VENV)
	@echo "$(GREEN)✓ Virtual environment created!$(RESET)"

install: venv
	@echo "$(YELLOW2)$(BOLD) Installing Fly-in dependencies...$(RESET)"
	uv sync
	@echo "$(GREEN)$(BOLD)✓ Dependencies installed!$(RESET)"

run:
	@echo "$(YELLOW)$(BOLD) Launching Fly-in...$(RESET)"
	uv run $(PYTHON) $(MAIN_SCRIPT) $(CONFIG_FILE)

debug:
	@echo "$(YELLOW)$(BOLD) Launching Fly-in in debug mode...$(RESET)"
	$(PYTHON) -m pdb $(MAIN_SCRIPT) $(CONFIG_FILE)

clean:
	@echo "$(YELLOW)$(BOLD) Cleaning temporary files and caches...$(RESET)"
	@if [ -d "venv" ]; then rm -rf venv && echo "$(RED)  ✓ Removed venv/$(RESET)"; fi
	@rm -rf dist/ build/ *.egg-info
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "$(GREEN)$(BOLD)✓ Cleanup complete!$(RESET)"

lint:
	@echo "$(YELLOW)$(BOLD)🔎 Running flake8...$(RESET)"
	$(PYTHON) -m flake8
	@echo "$(YELLOW2)$(BOLD)🔎 Running mypy...$(RESET)"
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
	@echo "$(GREEN)$(BOLD)✓ Lint complete!$(RESET)"

lint-strict:
	@echo "$(YELLOW)$(BOLD)🔎 Running flake8 (strict)...$(RESET)"
	$(PYTHON) -m flake8
	@echo "$(YELLOW2)$(BOLD)🔎 Running mypy (strict)...$(RESET)"
	$(PYTHON) -m mypy . --strict
	@echo "$(GREEN)$(BOLD)✓ Strict lint complete!$(RESET)"

help:
	@echo ""
	@echo "$(YELLOW)$(BOLD) Fly-in — Drone Routing Simulation$(RESET)"
	@echo "$(RED)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(RESET)"
	@echo "  $(YELLOW)make venv$(RESET)         - Setup virtual environment"
	@echo "  $(YELLOW2)make install$(RESET)      - Install project dependencies"
	@echo "  $(YELLOW)make run$(RESET)          - Run the simulation"
	@echo "  $(YELLOW2)make debug$(RESET)        - Run in debug mode (pdb)"
	@echo "  $(YELLOW)make clean$(RESET)        - Remove caches and temp files"
	@echo "  $(YELLOW2)make lint$(RESET)         - Run flake8 + mypy"
	@echo "  $(YELLOW)make lint-strict$(RESET)  - Run flake8 + mypy strict"
	@echo "  $(YELLOW2)make help$(RESET)         - Show this message"
	@echo "$(RED)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(RESET)"
	@echo ""