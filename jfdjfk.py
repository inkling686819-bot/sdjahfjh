content = content.replace(search_text, replace_text)
                        with open(full_path, "w", encoding="utf-8") as f:
                            f.write(content)
                        msg = f"✅ Đã sửa file: {full_path}"
                        print(msg)
dfhjf
