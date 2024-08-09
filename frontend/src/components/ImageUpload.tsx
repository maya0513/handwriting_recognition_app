import React, { useState } from 'react';
import axios from 'axios';

const ImageUpload: React.FC = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [prediction, setPrediction] = useState<number | null>(null);
    const [error, setError] = useState<string | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setSelectedFile(event.target.files[0]);
            setError(null);
        }
    };

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        if (!selectedFile) {
            setError('Please select a file');
            return;
        }

        const formData = new FormData();
        formData.append('image', selectedFile);

        try {
            const response = await axios.post('http://localhost:8000/api/predict/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setPrediction(response.data.prediction);
            setError(null);
        } catch (error) {
            console.error('Error uploading file:', error);
            if (axios.isAxiosError(error)) {
                if (error.response) {
                    // サーバーからのレスポンスがある場合
                    setError(`Error: ${error.response.status} - ${error.response.data}`);
                } else if (error.request) {
                    // リクエストは送信されたがレスポンスがない場合
                    setError('No response received from server. Please check your network connection.');
                } else {
                    // リクエストの設定中にエラーが発生した場合
                    setError(`Error setting up the request: ${error.message}`);
                }
            } else {
                setError('An unexpected error occurred. Please try again.');
            }
        }
    };

    return (
        <div className="image-upload">
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} accept="image/*" />
                <button type="submit">Upload and Predict</button>
            </form>
            {error && <p className="error">{error}</p>}
            {prediction !== null && <p className="prediction">Predicted digit: {prediction}</p>}
        </div>
    );
};

export default ImageUpload;