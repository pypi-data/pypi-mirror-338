from typing import Dict, Optional, List

from fi.api.auth import APIKeyAuth, ResponseHandler
from fi.api.types import HttpMethod, RequestConfig
from fi.kb.types import KnowledgeBaseConfig

from fi.utils.errors import InvalidAuthError
from fi.utils.routes import Routes

class KBResponseHandler(ResponseHandler[Dict, KnowledgeBaseConfig]):

    @classmethod
    def _parse_success(cls, response) -> Dict:
        """Handles responses for prompt requests"""
        data = response.json()

        if response.request.method == HttpMethod.GET.value:
            return response

        if response.request.method == HttpMethod.POST.value and response.url.endswith(
            Routes.knowledge_base.value
        ):
            return data["result"]
        
        if response.request.method == HttpMethod.PATCH.value and response.url.endswith(
            Routes.knowledge_base.value
        ):
            return data["result"]
        
        if response.request.method == HttpMethod.DELETE.value:
            return data
        
        return data
    
    @classmethod
    def _handle_error(cls, response) -> None:
        if response.status_code == 403:
            raise InvalidAuthError()
        else:
            response.raise_for_status()

class KnowledgeBaseClient(APIKeyAuth):

    def __init__(
        self,
        kbase: Optional[KnowledgeBaseConfig] = None,
        fi_api_key: Optional[str] = None,
        fi_secret_key: Optional[str] = None,
        fi_base_url: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            fi_api_key=fi_api_key,
            fi_secret_key=fi_secret_key,
            fi_base_url=fi_base_url,
            **kwargs,
        )
        self.kb = None
        if kbase and not kbase.id:
            try:
                self.kb = self._get_kb_from_name(kbase.name)
            except Exception:
                print("Knowlege Base not found in backend. Create a new knowledge base before running.")
        else:
            self.kb = kbase
            if self.kb:
                print(
                    f"Current Knowledge Base: {self.kb.name} does not exist in the backend. Please create it first before running."
                )
        
        print("Initialized Knowledge Base Client")

    def update_kb(self, name : Optional[str] = None, file_paths: Optional[List[str]] = []):
        try:
            import requests  
            
            if not self.kb:
                print("No kb provided. Please provide or create a kb before running.")
                return None

            if not file_paths:
                print("Files to be added not found.")

            method = HttpMethod.PATCH
            url = self._base_url + "/" + Routes.knowledge_base.value
            
            data = {}
            if name or self.kb:
                data.update({
                    "name": self.kb.name if not name else name,
                    "kb_id": self.kb.id
                })
            
            files = []
            
            try:
                if file_paths:
                    for file_path in file_paths:
                        file_name = file_path.split('/')[-1]
                        file_ext = file_path.split('.')[-1].lower()
                        
                        if file_ext not in ['pdf', 'docx', 'txt', 'rtf']:
                            print(f"Skipping unsupported file type: {file_ext} for {file_name}")
                            continue
                        
                        files.append(('file', (file_name, open(file_path, 'rb'), self._get_content_type(file_ext))))
                
                headers = {
                    'Accept': 'application/json',
                    'X-Api-Key': self._fi_api_key,
                    'X-Secret-Key': self._fi_secret_key,
                }
                
                response = requests.patch(
                    url=url,
                    data=data,
                    files=files,  
                    headers=headers,
                    timeout=30
                )
                
                if response.status_code != 200:
                    raise Exception(f"Request failed with status code {response.status_code}")
                    
                response_data = response.json()
                result = response_data.get("result", {})
                
                if result:
                    self.kb.id = result.get("id", self.kb.id)
                    self.kb.name = result.get("name", self.kb.name)
                    if "files" in result:
                        self.kb.files = result["files"]

                return self
            
            finally:
                for file_tuple in files:
                    if hasattr(file_tuple[1][1], 'close'):
                        file_tuple[1][1].close()
            
        except Exception as e:
            print(f"Failed to add files to the Knowledge Base: {str(e)}")
            return None

    def delete_files_from_kb(self, file_ids):
        try:
            if not self.kb:
                print("No knowledge base provided. Please provide a knowledge base before running.")
                return None
                
            if not file_ids:
                print("Files to be deleted not found. Please provide correct File IDs.")
                return self
                
            method = HttpMethod.DELETE
            url = self._base_url + "/" + Routes.knowledge_base_files.value
            
            data = {
                "file_ids": file_ids,
                "kb_id": self.kb.id
            }
            
            response = self.request(
                config=RequestConfig(
                    method=method,
                    url=url,
                    json=data,
                    headers={'Content-Type': 'application/json'}
                ),
                response_handler=KBResponseHandler,
            )


            return self
        
        except Exception as e:
            print(f"Failed to delete files from Knowledge Base: {str(e)}")
            return None

    def delete_kb(self, kb_ids : Optional[str] = None):
        try:        
            if not self.kb and not kb_ids:
                print("No knowledge base provided. Please provide a knowledge base before running.")
                return None
            
            method = HttpMethod.DELETE
            url = self._base_url + "/" + Routes.knowledge_base.value       
            json = {
                "kb_ids": [self.kb.id]
            }
            
            
            response = self.request(
                config=RequestConfig(
                    method=method,
                    url=url,
                    json=json,
                    headers={'Content-Type': 'application/json'}
                ),
                response_handler=KBResponseHandler,
            )

            self.kb = None
            
            return self
        
        except Exception as e:
            print(f"Failed to delete Knowledge Base: {str(e)}")
            return None

    def create(self, name : Optional[str] = None, file_paths : Optional[List[str]] = []):
        """
        Create a Knowledge Base and return the Knowledge Base client
        Args:
            file_paths: "List of file paths to be uploaded 
        """
        import requests
        
        if self.kb and self.kb.id:
            print(
                f"Knowledge Base, {self.kb.name}, already exists in the backend. Please use a different name to create a new Knowledge Base."
            )
            return self
        
        data = {}
        if name or self.kb:
            data.update({
                "name": self.kb.name if not name else name
            })
            
        method = HttpMethod.POST
        url = self._base_url + "/" + Routes.knowledge_base.value
        
        files = []
        
        try:
            if file_paths:
                for file_path in file_paths:
                    file_name = file_path.split('/')[-1]
                    file_ext = file_path.split('.')[-1].lower()
                    
                    if file_ext not in ['pdf', 'docx', 'txt', 'rtf']:
                        print(f"Skipping unsupported file type: {file_ext} for {file_name}")
                        continue
                    
                    files.append(('file', (file_name, open(file_path, 'rb'), self._get_content_type(file_ext))))
            
            headers = {
                'Accept': 'application/json',
                'X-Api-Key': self._fi_api_key,
                'X-Secret-Key': self._fi_secret_key,
            }
            
            response = requests.post(
                url=url,
                data=data,
                files=files,  
                headers=headers,
                timeout=30
            )
            
            if response.status_code != 200:
                raise Exception(f"Request failed with status code {response.status_code}")
                
            response_data = response.json()
            result = response_data.get("result", {})
            
            self.kb = KnowledgeBaseConfig(
                id=result.get("kbId"), 
                name=result.get("kbName"), 
                files=result.get("fileIds", [])
            )
            return self
            
        finally:
            for file_tuple in files:
                if hasattr(file_tuple[1][1], 'close'):
                    file_tuple[1][1].close()

    def _get_content_type(self, file_ext):
        """Get the correct content type for a file extension"""
        content_types = {
            "pdf": "application/pdf",
            "rtf": "application/rtf",
            "txt": "text/plain",
            "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        }
        return content_types.get(file_ext, "application/octet-stream")

    def _get_kb_from_name(self, kb_name):
        response = self.request(
            config=RequestConfig(
                method=HttpMethod.GET,
                url=self._base_url + "/" + Routes.knowledge_base_list.value,
                params={"search": kb_name},
            ),
            response_handler=KBResponseHandler,
        )
        return response