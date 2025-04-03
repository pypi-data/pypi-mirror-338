import toml
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from deepdiff import DeepDiff


class ProjectToml:
    def __init__(self, path: Union[str, Path] = "pyproject.toml"):
        self.path = Path(path)
        self._data: Dict[str, Any] = {}
        self.load()

    def load(self):
        if not self.path.exists():
            raise FileNotFoundError(f"No pyproject.toml found at {self.path}")
        self._data = toml.load(self.path)

    def save(self):
        with self.path.open("w", encoding="utf-8") as f:
            toml.dump(self._data, f)

    def reload(self):
        self.load()

    def as_dict(self) -> Dict[str, Any]:
        return self._data

    def diff(self, other: Union['ProjectToml', Dict[str, Any], str, Path]) -> DeepDiff:
        if isinstance(other, ProjectToml):
            other_data = other.as_dict()
        elif isinstance(other, (str, Path)):
            other_data = toml.load(Path(other))
        elif isinstance(other, dict):
            other_data = other
        else:
            raise TypeError(f"Unsupported type for diff: {type(other)}")

        return DeepDiff(self._data, other_data, view='tree')

    @property
    def project(self) -> Dict[str, Any]:
        return self._data.setdefault("project", {})

    # Core Metadata
    @property
    def name(self) -> Optional[str]:
        return self.project.get("name")

    @property
    def version(self) -> Optional[str]:
        return self.project.get("version")

    @property
    def description(self) -> Optional[str]:
        return self.project.get("description")

    @property
    def readme(self) -> Union[str, Dict[str, Any], None]:
        return self.project.get("readme")

    @property
    def license(self) -> Union[str, Dict[str, str], None]:
        return self.project.get("license")

    @property
    def requires_python(self) -> Optional[str]:
        return self.project.get("requires-python")

    @property
    def keywords(self) -> List[str]:
        return self.project.get("keywords", [])

    @property
    def classifiers(self) -> List[str]:
        return self.project.get("classifiers", [])

    @property
    def dynamic(self) -> List[str]:
        return self.project.get("dynamic", [])

    # People
    @property
    def authors(self) -> List[Dict[str, str]]:
        return self.project.get("authors", [])

    @property
    def maintainers(self) -> List[Dict[str, str]]:
        return self.project.get("maintainers", [])

    # Dependencies
    @property
    def dependencies(self) -> List[str]:
        return self.project.get("dependencies", [])

    @property
    def optional_dependencies(self) -> Dict[str, List[str]]:
        return self.project.get("optional-dependencies", {})

    # Project URLs
    @property
    def urls(self) -> Dict[str, str]:
        return self.project.get("urls", {})

    # Entry Points
    @property
    def scripts(self) -> Dict[str, str]:
        return self.project.get("scripts", {})

    @property
    def gui_scripts(self) -> Dict[str, str]:
        return self.project.get("gui-scripts", {})

    @property
    def entry_points(self) -> Dict[str, Dict[str, str]]:
        return self.project.get("entry-points", {})

    # Modifiers
    def add_author(self, name: str, email: Optional[str] = None):
        entry = {"name": name}
        if email:
            entry["email"] = email
        self.authors.append(entry)

    def add_dependency(self, dep: str):
        self.project.setdefault("dependencies", []).append(dep)

    def remove_dependency(self, name: str):
        deps = self.project.get("dependencies", [])
        updated = [d for d in deps if not d.split("==")[0].split(">=")[0].split("<=")[0].strip() == name]
        self.project["dependencies"] = updated


    def add_classifier(self, classifier: str):
        self.project.setdefault("classifiers", []).append(classifier)

    def add_script(self, name: str, entry: str):
        self.project.setdefault("scripts", {})[name] = entry

    def add_entry_point(self, group: str, name: str, entry: str):
        ep = self.project.setdefault("entry-points", {}).setdefault(group, {})
        ep[name] = entry

    # Build System
    @property
    def build_system(self) -> Dict[str, Any]:
        return self._data.setdefault("build-system", {})

    @property
    def build_backend(self) -> Optional[str]:
        return self.build_system.get("build-backend")

    @property
    def requires(self) -> List[str]:
        return self.build_system.get("requires", [])

    # Tool section (dynamic tools like poetry, black, etc.)
    def get_tool(self, tool_name: str) -> Dict[str, Any]:
        return self._data.setdefault("tool", {}).setdefault(tool_name, {})

    def set_tool_config(self, tool_name: str, config: Dict[str, Any]):
        self._data.setdefault("tool", {})[tool_name] = config

    def has_tool(self, tool_name: str) -> bool:
        return tool_name in self._data.get("tool", {})

    @property
    def poetry(self) -> Dict[str, Any]:
        return self.get_tool("poetry")

    @property
    def hatch(self) -> Dict[str, Any]:
        return self.get_tool("hatch")

    @property
    def ruff(self) -> Dict[str, Any]:
        return self.get_tool("ruff")

    def __repr__(self):
        return f"<ProjectToml path={self.path} name={self.name} version={self.version}>"


if __name__ == '__main__':
    # Example usage
    project = ProjectToml()
    print(project.name)
    print(project.version)
    print(project.dependencies)
    project.add_dependency("requests")
    project.save()
    print(project.dependencies)
    project.remove_dependency("requests")
    project.save()
    print(project.as_dict())